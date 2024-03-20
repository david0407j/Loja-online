from django.urls import path

from loja.produtos.views import produto_alguma_coisa, meu_carrinho, adicionar_no_carrinho, variedade_infantil
 
app_name = 'produtos'

urlpatterns = [
    path('meucarrinho', meu_carrinho),
    path('meucarrinho/adicionar/<int:produto_id>', adicionar_no_carrinho, name='carrinho.adicionar'),
    path('<slug:slug>', produto_alguma_coisa, name='Produto'),
    path('', variedade_infantil, name='produto'),
 ]
