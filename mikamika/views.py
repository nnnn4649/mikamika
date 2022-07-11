from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from .forms import MikamikaForm
from .models import Mikamika

class IndexView(TemplateView):
    template_name = 'index.html'

class MikamikaCreateView(CreateView):
    template_name = 'mikamika_create.html'
    form_class = MikamikaForm
    success_url = reverse_lazy('mikamika:mikamika_create_complete')

class MikamikaCreateCompleteView(TemplateView):
    template_name = 'mikamika_create_complete.html'

class MikamikaListView(ListView):
    template_name = 'mikamika_list.html'
    model = Mikamika

class MikamikaDetailView(DetailView):
    template_name = 'mikamika_detail.html'
    model = Mikamika