from django.urls import path

from loja.modelos.views import  infantil



app_name = 'modelos'
urlpatterns = [
    path('<slug:slug>', infantil, name='infantil'),
]