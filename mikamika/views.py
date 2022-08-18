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
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
import random
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from collections import Counter
import re

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
     
     ustore = Mikamika.objects.values_list("store" ,"hyouka").filter(create_user=uflag)
     
     count   = len(ustore)
     mstore  = list(ustore)
     for index in range(count):
         mstore[index] = Mikamika.objects.filter(store__in=ustore[index],hyouka__in=ustore[index]).exclude(create_user=uflag)
    
     matti = max(mstore[index],key=mstore.count)
     
     mflag = matti.create_user.id
     mgstore = Mikamika.objects.values_list("store",flat=True).filter(hyouka='1',create_user=mflag)

     context = {'gcount'    :  gcount,
                'scount'    :  scount,
                'matti'     :  matti,
                'uflag'     :  uflag,
                'mgstore'   :  mgstore,
                'mflag'     :  mflag,}
     return render(request, template_name , context)

@login_required
def  mikamika_ulist(request):
     template_name = 'ulist.html'

     uname = request.user
     uflag = uname.id

     gustore = Mikamika.objects.values_list("store",flat=True).filter(hyouka='1',create_user=uflag)
     sstore  = Mikamika.objects.values_list("store",flat=True).filter(hyouka='0',create_user=uflag)

     gupk = Mikamika.objects.values_list("id",flat=True).filter(hyouka='1',create_user=uflag)
     supk = Mikamika.objects.values_list("id",flat=True).filter(hyouka='0',create_user=uflag)
     
     mgustore = list(zip(gupk,gustore)) 
     msustore = list(zip(supk,sstore))
    
     context = {'mgustore'  : mgustore,
                'msustore'  : msustore,
                'sstore'   :  sstore,
                'supk'     :  supk,
                'gupk'     :  gupk,
                'gustore'  :  gustore,}

     return render(request, template_name , context)


class MikamikaListView(ListView): 
      template_name = 'mikamika_list.html'
      model = Mikamika


@login_required
def  mikamika_udetail(request):
      template_name = 'udetail.html'
      gustore = 1
      sstore = 1
      context = {'gustore'  :  gustore,
                 'sstore'   :   sstore,}
      return render(request, template_name , context)

#@login_required
class UupdateView(UpdateView):
      template_name = 'uupdate.html'
      model = Mikamika
      fields = ('store', 'bikou','hyouka','todou')
      success_url = reverse_lazy('mikamika:mikamika_ulist')

      def form_valid(self, form):
          mikamika = form.save(commit=False)
          mikamika.updated_at = timezone.now()
          mikamika.save()
          return super().form_valid(form)


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

