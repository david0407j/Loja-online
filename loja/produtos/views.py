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

    item_existente = CarrinhoItem.objects.filter(carrinho=meu_carrinho, produto=produto).first()
    if not item_existente:
        item_existente = CarrinhoItem(produto=produto, quantidade=0, carrinho=meu_carrinho)

    item_existente.quantidade += 1
    item_existente.save()

    meu_carrinho = Carrinho.objects.filter(user=request.user).first()
    context={
        'meu_carrinho': meu_carrinho,
        'produtos_do_carrinho': CarrinhoItem.objects.filter(carrinho=meu_carrinho).order_by("-id"),
    }

    return render(request, 'produtos/meu_carrinho.html', context=context)

def excluir_item(request, item_id: int):
    meu_carrinho = Carrinho.objects.filter(user=request.user).first()

    try:
        #produto = Produto.objects.get(id=produto_id)
        CarrinhoItem.objects.get(id=item_id).delete()

        # TODO: remover este DRY
        context={
            'meu_carrinho': meu_carrinho,
            'produtos_do_carrinho': CarrinhoItem.objects.filter(carrinho=meu_carrinho),
        }        
        return render(request, 'produtos/meu_carrinho.html', context=context)

    except:
        # TODO:
        return render(request, 'produtos/meu_carrinho.html', context=context)



def remover_do_carrinho(request, produto_id: int):
    meu_carrinho = Carrinho.objects.filter(user=request.user).first()
    produto = Produto.objects.get(id=produto_id)

    item_existente = CarrinhoItem.objects.filter(carrinho=meu_carrinho, produto=produto).first()
    if item_existente:
        item_existente.quantidade -= 1
        item_existente.save()

        if item_existente.quantidade == 0:
            item_existente.delete()

    meu_carrinho = Carrinho.objects.filter(user=request.user).first()
    context={
        'meu_carrinho': meu_carrinho,
        'produtos_do_carrinho': CarrinhoItem.objects.filter(carrinho=meu_carrinho).order_by("-id"),
    }
    return render(request, 'produtos/meu_carrinho.html', context=context)


def calcular_total_carrinho(request):
    carrinho = CarrinhoItem.objects.all()
    total_compra = sum(item.total_item for item in carrinho)
    return render(request, 'produtos/meu_carrinho.html', {'carrinho': carrinho, 'total_compra': total_compra})