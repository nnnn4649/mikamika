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

class IndexView(TemplateView):
    template_name = 'index.html'

class FaView(CreateView):
    template_name = 'fa.html'
    form_class = MikamikaForm
    model = Mikamika

    def mikamika_create(request):
      store = Mikamika.objects.filter(hyouka='0').order_by('created_at').first()
      store_list = Mikamika.objects.all()
      return render(request, 'fa.html', {'store_list':store_list})
    success_url = reverse_lazy('mikamika:mikamika_create_complete')
    

class MikamikaCreateCompleteView(TemplateView):
    template_name = 'mikamika_create_complete.html'

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