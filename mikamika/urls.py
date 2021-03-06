from django.urls import path
from . import views
 
app_name = 'mikamika'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('tokoo/', views.FaView.as_view(), name='tokoo'),
    path('mikamika/create/', views.mikamika_create, name='mikamika_create'),
    path('mikamika/create/complete/', views.MikamikaCreateCompleteView.as_view(), name='mikamika_create_complete'),
    path('mikamika/list/', views.mikamika_user, name='mikamika_user'),# 新
    path('mikamika/detail/<uuid:pk>/', views.MikamikaDetailView.as_view(), name='mikamika_detail'), # 追記
    path('mikamika/update/<uuid:pk>/', views.MikamikaUpdateView.as_view(), name='mikamika_update'), #追記
    path('mikamika/delete/<uuid:pk>/', views.MikamikaDeleteView.as_view(), name='mikamika_delete'), #追加
]