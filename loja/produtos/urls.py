from django.urls import path
from loja.produtos.views import variedade



app_name = 'produtos'
urlpatterns = [
    path('<slug:nome>', variedade, name='variedade'),
]
