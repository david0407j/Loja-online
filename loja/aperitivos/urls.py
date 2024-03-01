from django.urls import path
from loja.aperitivos.views import  feminina, masculino

app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', masculino, name='masculino'),
    path('', feminina, name='masculino'),
]