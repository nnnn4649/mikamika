from ssl import _create_unverified_context
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .forms import MikamikaForm
from .models import Mikamika
from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
import random
from django.db.models import Q
from django.contrib.auth.decorators import login_required

class IndexView(TemplateView):
    template_name = 'index.html'

class FaView(LoginRequiredMixin, CreateView):
      template_name = 'tokoo.html'
      login_url = '/account/login/'
      form_class = MikamikaForm
      model = Mikamika
      success_url = reverse_lazy('mikamika:mikamika_create_complete')

      def form_valid(self, form):
          mikamika =  form.save(commit=False)
          mikamika.create_user=self.request.user
          mikamika.save()
          return super().form_valid(form)

class UserView(LoginRequiredMixin, CreateView):
      template_name = 'user.html'
      login_url = '/account/login/'
      form_class = MikamikaForm
      model = Mikamika
      success_url = reverse_lazy('mikamika:mikamika_create_complete')

      def form_valid(self, form):
          mikamika =  form.save(commit=False)
          mikamika.create_user=self.request.user
          mikamika.save()
          return super().form_valid(form)

def mikamika_create(request):
    template_name = 'fa.html'
    
    sostore  = Mikamika.objects.values_list("create_user").filter(hyouka='0')
    gstore   = Mikamika.objects.values_list("create_user").filter(hyouka='1')

    sgstore = set(gstore) & set(sostore)
    setuflag = random.sample(sgstore,k=1)
    uflag = setuflag[0]
    usostore  = Mikamika.objects.values_list("store",flat=True).filter(hyouka='0',create_user=uflag).order_by('?').first()
    ugstore   = Mikamika.objects.values_list("store",flat=True).filter(hyouka='1',create_user=uflag).order_by('?').first()

    context = {'usostore' : usostore,
               'ugstore' : ugstore,}
    return render(request, template_name , context)
    
class MikamikaCreateCompleteView(TemplateView):
    template_name = 'mikamika_create_complete.html'


@login_required
def  mikamika_user(request):
     template_name = 'user.html'
     uflag = request.user
     gcount = Mikamika.objects.values_list("store",flat=True).filter(hyouka='1',create_user=uflag).count()
     scount = Mikamika.objects.values_list("store",flat=True).filter(hyouka='0',create_user=uflag).count()
     
     ustore   = Mikamika.objects.values_list("store" ,flat=True).filter(create_user=uflag)
     uhyouka  = Mikamika.objects.values_list("hyouka",flat=True).filter(create_user=uflag)
     sustore  = set(ustore)
     mstore   = Mikamika.objects.filter(store__in=sustore)

     for mmstore in mstore:
        if mmstore == 'nnnn4649':
           print('????????????????????????')
        else:
           mstore = mstore
     matti1  = Mikamika.objects.filter(store__in=sustore)
     context = {'gcount'   :  gcount,
               'scount'    :  scount,
               'matti1'    :  matti1,
               'mstore'    :  mstore,
               'uflag'     :  uflag,}
     return render(request, template_name , context)

class MikamikaListView(ListView): 
      template_name = 'mikamika_list.html'
      model = Mikamika

class MikamikaDetailView(DetailView):
    template_name = 'mikamika_detail.html'
    model = Mikamika

class MikamikaUpdateView(UpdateView):
    template_name = 'mikamika_update.html'
    model = Mikamika
    fields = ('date', 'title', 'text',)
    success_url = reverse_lazy('mikamika:mikamika_list')

    def form_valid(self, form):
        mikamika = form.save(commit=False)
        mikamika.updated_at = timezone.now()
        mikamika.save()
        return super().form_valid(form)

class MikamikaDeleteView(DeleteView):
    template_name = 'mikamika_delete.html'
    model = Mikamika
    success_url = reverse_lazy('mikamika:mikamika_list')

