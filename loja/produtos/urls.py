from django.urls import path
from loja.produtos import views

app_name = 'produtos'

urlpatterns = [
    path('meucarrinho', views.meu_carrinho),
    path('meucarrinho/adicionar/<int:produto_id>', views.adicionar_no_carrinho, name='carrinho.adicionar'),
    path('<str:nome_categoria>', views.produto_alguma_coisa, name='produto'),
    path('carrinho/remover/<int:produto_id>/', views.remover_do_carrinho, name='carrinho.remover'),
    path('meucarrinho/excluir/<item_id>/', views.excluir_item, name='carrinho.excluir'),
    path('meucarrinho/compra/finalizar', views.finalizar_compra_whatsapp, name="carrinho.finalizar.compra"),
    path('adicionar/<int:produto_id>/', views.adicionar_no_carrinho, name='adicionar_no_carrinho'),
]
