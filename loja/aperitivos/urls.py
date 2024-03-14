from django.urls import path
from loja.aperitivos.views import   Produto

app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', Produto, name='Produto'),
   
]