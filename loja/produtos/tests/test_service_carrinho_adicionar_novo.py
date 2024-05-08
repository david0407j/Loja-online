import pytest

from itertools import cycle
from model_bakery import baker

from loja.produtos.models import Tamanho, Categoria, Produto, Carrinho, CarrinhoItem
from loja.produtos.service import carrinho


@pytest.mark.django_db
def test_deve_adicionar_um_novo_item_no_carrinho(user_joao):
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

    # Então
    carrinho_do_joao = Carrinho.objects.filter(user=user_joao).first()
    items_do_carrinho = CarrinhoItem.objects.filter(carrinho=carrinho_do_joao).order_by("-id")
    item1 = items_do_carrinho.first()

    assert len(items_do_carrinho) == 1
    assert item1.produto == camiseta1
    assert item1.quantidade == 2


def test_deve_adicionar_dois_produtos_no_carrinho(user_joao):
    # DADO duas camisetas
    camisetas = baker.make('Categoria', nome="camisetas")
    baker.make('Tamanho', descricao=cycle(["P", "M", "G"]))

    camiseta1 = baker.make(
        'Produto',
        categoria=camisetas,
        descricao='Camiseta do Brasil Amarela',
        nome='camiseta1',
        valor=102.00,
    )

    camiseta2 = baker.make(
        'Produto',
        categoria=camisetas,
        descricao='Camiseta do Brasil Verde',
        nome='camiseta2',
        valor=104.00,
    )

    # Quando adicionamos no carrinho
    carrinho.adicionar_item(user_joao, camiseta1.id, 2, "P")
    carrinho.adicionar_item(user_joao, camiseta1.id, 1, "G")

    # Então
    carrinho_do_joao = Carrinho.objects.filter(user=user_joao).first()
    items_do_carrinho = CarrinhoItem.objects.filter(carrinho=carrinho_do_joao).order_by("id")
    item1, item2 = items_do_carrinho

    assert len(items_do_carrinho) == 2
    assert item1.produto == camiseta1
    assert item1.tamanho == "P"
    assert item1.quantidade == 2

    assert item2.produto == camiseta1
    assert item1.tamanho == "G"
    assert item2.quantidade == 41
