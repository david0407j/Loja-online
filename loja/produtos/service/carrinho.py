from loja.produtos.models import Produto, Carrinho, CarrinhoItem


def adicionar_item(user, produto_id, quantidade, tamanho):
    meu_carrinho = Carrinho.objects.filter(user=user).first()
    if not meu_carrinho:
        meu_carrinho = Carrinho.objects.create(user=user)

    produto = Produto.objects.get(id=produto_id)

    novo_item = CarrinhoItem.objects.filter(carrinho=meu_carrinho, produto=produto).first()
    if not novo_item:
        novo_item = CarrinhoItem(produto=produto, quantidade=0, carrinho=meu_carrinho)

    novo_item.quantidade += quantidade
    novo_item.save()

    return novo_item


def obter_carrinho(user):
    meu_carrinho = Carrinho.objects.filter(user=user).first()
    if not meu_carrinho:
        meu_carrinho = Carrinho.objects.create(user=user)

    items_do_carrinho = CarrinhoItem.objects.filter(carrinho=meu_carrinho).order_by("-id")
    return {
        "carrinho": meu_carrinho,
        "items": items_do_carrinho,
        "total": sum([item.total_item for item in items_do_carrinho])
    }
