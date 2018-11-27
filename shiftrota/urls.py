from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home,name='homepage'),
    url(r'^home', views.home,name='shift-rota'),
    url(r'^upload', views.upload_rota, name='upload_excel'),
    url(r'^plan/new/', views.plan_new_v,name='plan_new_v'),
]
