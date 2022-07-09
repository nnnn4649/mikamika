from django.urls import path
from . import views
 
app_name = 'mikamika'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('mikamika/create/', views.MikamikaCreateView.as_view(), name='mikamika_create'),
    path('mikamika/create/complete/', views.MikamikaCreateCompleteView.as_view(), name='mikamika_create_complete'),
]