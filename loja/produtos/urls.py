from django.urls import path
from loja.produtos.views import outros



app_name = 'produtos'
urlpatterns = [
    path('<slug:slug>', outros, name='outros'),
]
