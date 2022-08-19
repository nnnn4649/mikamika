from django.urls import path
from . import views
 
app_name = 'mikamika'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('tokoo/', views.FaView.as_view(), name='tokoo'),
    path('mikamika/create/', views.mikamika_create, name='mikamika_create'),
    path('mikamika/todoulist/', views.mikamika_todoulist, name='mikamika_todoulist'),#新６
    path('mikamika/create/complete/', views.MikamikaCreateCompleteView.as_view(), name='mikamika_create_complete'),
    path('mikamika/user/', views.mikamika_user, name='mikamika_user'),# 新
    path('mikamika/ulist/', views.mikamika_ulist, name='mikamika_ulist'),# 新2
    path('mikamika/udetail/', views.mikamika_udetail, name='mikamika_udetail'),# 新3
    path('mikamika/detail/<uuid:pk>/', views.MikamikaDetailView.as_view(), name='mikamika_detail'),# 追記
    path('mikamika/uupdate/<uuid:pk>/', views.UupdateView.as_view(), name='mikamika_uupdate'), #新４
    path('mikamika/udelete/<uuid:pk>/', views.UDeleteView.as_view(), name='mikamika_udelete'),#新５
    path('mikamika/list/<uuid:pk>/', views.MikamikaListView.as_view(), name='mikamika_list'),#追加
]