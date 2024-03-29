from django.urls import path

from loja.produtos.views import produto_alguma_coisa, meu_carrinho, adicionar_no_carrinho, remover_do_carrinho
 
app_name = 'produtos'

urlpatterns = [
    path('meucarrinho', meu_carrinho),
    path('meucarrinho/adicionar/<int:produto_id>', adicionar_no_carrinho, name='carrinho.adicionar'),
    path('<str:nome_categoria>', produto_alguma_coisa, name='produto'),
    path('carrinho/remover/<int:item_id>/', remover_do_carrinho, name='remover_do_carrinho'),
 ]
 