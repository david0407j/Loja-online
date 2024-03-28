from django.shortcuts import render
from loja.produtos.models import  Produto, Carrinho, Categoria, CarrinhoItem
 

def produto_alguma_coisa(request, nome_categoria):
    categoria = Categoria.objects.filter(nome__iexact=nome_categoria).first()
    if not categoria:
        categorias_validas = [c.nome for c in Categoria.objects.all()]
        raise Exception(f"Categoria '{nome_categoria}' nao encontrada. Utilize uma das {categorias_validas}")

    produtos_da_categoria = Produto.objects.filter(categoria_id=categoria.id)
    context={
        'camisetas': produtos_da_categoria,
        'categoria': categoria,
    }
    return render(request, 'produtos/produtos.html', context=context)
 
 
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

def remover_do_carrinho(request, produto_id: int):
    carrinho = Carrinho.objects.filter(user=request.user).first()
    if not carrinho:
        carrinho = Carrinho.objects.create(user=request.user)

    produto = Produto.objects.get(id=produto_id)
    try:
        item = CarrinhoItem.objects.get(produto=produto)
        item.quantidade -= 1
        item.save()
        if item.quantidade <= 0:
            item.delete()
    except:
        return render(request, 'produtos/meu_carrinho.html', context={'carrinho': carrinho})
    return render(request, 'produtos/meu_carrinho.html', context={'carrinho': carrinho})


