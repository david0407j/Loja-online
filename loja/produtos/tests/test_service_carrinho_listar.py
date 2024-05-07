import pytest

from itertools import cycle
from model_bakery import baker

from loja.produtos.models import Tamanho, Categoria, Produto, Carrinho, CarrinhoItem
from loja.produtos.service import carrinho


@pytest.mark.django_db
def test_deve_listar_total_do_carrinho(user_joao):
    # DADO um tamanho de camiseta e sua categoria
    camisetas = Categoria.objects.create(nome="camisetas")
    pequeno = Tamanho.objects.create(descricao="P")
    camiseta1 = Produto.objects.create(
        categoria=camisetas,
        descricao='Camiseta Brasil Amarela',
        nome='camiseta1',
        valor=102.00,
    )

    camiseta1.tamanhos.add(pequeno)

    # Quando adicionamos no carrinho
    carrinho.adicionar_item(user_joao, camiseta1.id, 2, "P")
    carrinho_joao = carrinho.obter_carrinho(user_joao)

    # Então
    assert len(carrinho_joao["items"]) == 1
    assert carrinho_joao["total"] == 2 * 102
