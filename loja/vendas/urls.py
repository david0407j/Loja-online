from django.urls import path
from loja.vendas.views import infantil, masculino
from loja.vendas.views import femenina
from loja.vendas.views import produtos


app_name = 'vendas'
urlpatterns = [
    path('<slug:nome>', masculino, name='masculino'),
    path('<slug:nome>', femenina, name='femenina'),
    path('<slug:nome>', produtos, name='produtos'),
    path('<slug:nome>', infantil, name='infantil'),
]