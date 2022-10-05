from django.urls import path
from . import views
 
app_name = 'mikamika'
urlpatterns = [
    path('', views.Index, name='index'),#index/
    path('tokoo/', views.TokooView.as_view(), name='tokoo'),
    path('mikamika/create/<ttdou>/<tstore>/', views.mikamika_create, name='mikamika_create'),
    path('mikamika/create2/<ttdou>/<tstore>/<tgtdou>/<tgstore>/', views.mikamika_create2, name='mikamika_create2'),#新
    path('mikamika/create3/<tgtdou>/<tgstore>/', views.mikamika_create3, name='mikamika_create3'),#新
    path('mikamika/create0/<mttdou>/<mtstore>/', views.mikamika_create0, name='mikamika_create0'),#新
    path('mikamika/create/complete/', views.MikamikaCreateCompleteView.as_view(), name='mikamika_create_complete'),
    path('mikamika/user/', views.mikamika_user, name='mikamika_user'),# 新
    path('mikamika/ulist/', views.mikamika_ulist, name='mikamika_ulist'),# 新2
    path('mikamika/udetail/', views.mikamika_udetail, name='mikamika_udetail'),# 新3
    path('mikamika/detail/<uuid:pk>/', views.MikamikaDetailView.as_view(), name='mikamika_detail'),# 追記
    path('mikamika/uupdate/<uuid:pk>/', views.UupdateView.as_view(), name='mikamika_uupdate'), #新４
    path('mikamika/udelete/<uuid:pk>/', views.UDeleteView.as_view(), name='mikamika_udelete'),#新５
    path('mikamika/list/<uuid:pk>/', views.MikamikaListView.as_view(), name='mikamika_list'),#追加
    path('mikamika/upload/', views.mikamika_upload, name='mikamika_upload'),
    path('mikamika/chat/', views.mikamika_chat, name='mikamika_chat'),
    path('mikamika/signup/', views.SignUpView.as_view(), name='mikamika_signup'),
    path('mikamika/create4/', views.mikamika_create4, name='mikamika_create4'),
]