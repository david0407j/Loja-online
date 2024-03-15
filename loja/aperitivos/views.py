from django.shortcuts import render
from loja.aperitivos.models import  Produto, Carrinho, CarrinhoItem 
 
 

def produto_alguma_coisa(request, slug):
    produtos = Produto.objects.all()
    return render(request, 'aperitivos/masculino.html', context={'masculinos': produtos})
 
 
def meu_carrinho(request):
    meu_carrinho = Carrinho.objects.filter(user=request.user).first()
    if not meu_carrinho:
        meu_carrinho = Carrinho.objects.create(user=request.user)

    return render(request, 'aperitivos/meu_carrinho.html', context={'meu_carrinho': meu_carrinho})


def adicionar_no_carrinho(request, produto_id: int):
    meu_carrinho = Carrinho.objects.filter(user=request.user).first()
    if not meu_carrinho:
        meu_carrinho = Carrinho.objects.create(user=request.user)

    produto = Produto.objects.get(id=produto_id)

    novo_item = CarrinhoItem(produto=produto, quantidade=1, carrinho=meu_carrinho)
    novo_item.save()
    meu_carrinho = Carrinho.objects.filter(user=request.user).first()

    return render(request, 'aperitivos/meu_carrinho.html', context={'meu_carrinho': meu_carrinho})


