from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='shift-rota'),
    path('upload', views.upload_rota, name='upload_excel')
]
