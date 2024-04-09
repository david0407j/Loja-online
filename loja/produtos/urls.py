from django.urls import path
from loja.produtos.views import (adicionar_no_carrinho, excluir_item, meu_carrinho,calcular_total_carrinho,
    produto_alguma_coisa, remover_do_carrinho)

app_name = 'produtos'

urlpatterns = [
    path('meucarrinho', meu_carrinho),
    path('meucarrinho/adicionar/<int:produto_id>', adicionar_no_carrinho, name='carrinho.adicionar'),
    path('<str:nome_categoria>', produto_alguma_coisa, name='produto'),
    path('carrinho/remover/<int:produto_id>/', remover_do_carrinho, name='carrinho.remover'),
    path('meucarrinho/excluir/<item_id>/', excluir_item, name='carrinho.excluir'),
    #path('meucarrinho/finalizar/<item_id>/', calcular_total_carrinho, name='carrinho.finalizar'),#
]

 