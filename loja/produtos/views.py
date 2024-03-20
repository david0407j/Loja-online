from django.shortcuts import render
from loja.produtos.models import  Produto, Carrinho, CarrinhoItem

def variedade_infantil(request):
    produtos = Produto.objects.order_by('criado_em').all()
    return render(request, 'produtos/produtos.html', context={'infantil': produtos})
 

def produto_alguma_coisa(request, slug):
    produtos = Produto.objects.all()
    return render(request, 'produtos/masculino.html', context={'masculinos': produtos})
 
 
def meu_carrinho(request):
    meu_carrinho = Carrinho.objects.filter(user=request.user).first()
    if not meu_carrinho:
        meu_carrinho = Carrinho.objects.create(user=request.user)

    return render(request, 'produtos/meu_carrinho.html', context={'meu_carrinho': meu_carrinho})


def adicionar_no_carrinho(request, produto_id: int):
    meu_carrinho = Carrinho.objects.filter(user=request.user).first()
    if not meu_carrinho:
        meu_carrinho = Carrinho.objects.create(user=request.user)

    produto = Produto.objects.get(id=produto_id)

    novo_item = CarrinhoItem(produto=produto, quantidade=1, carrinho=meu_carrinho)
    novo_item.save()
    meu_carrinho = Carrinho.objects.filter(user=request.user).first()

    return render(request, 'produtos/meu_carrinho.html', context={'meu_carrinho': meu_carrinho})


