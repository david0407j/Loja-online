from django.shortcuts import render, redirect
from loja.produtos.models import Carrinho, CarrinhoItem, Categoria, Produto
 

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


def obter_total_carrinho(items_do_carrinho):
    return sum([item.total_item for item in items_do_carrinho])


def adicionar_no_carrinho(request, produto_id: int):
    carrinho = CarrinhoItem.objects.filter(carrinho__user=request.user)
    tamanho = request.POST.get('tamanho')
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
    items_do_carrinho = CarrinhoItem.objects.filter(carrinho=meu_carrinho).order_by("-id")
    total_compra = obter_total_carrinho(items_do_carrinho)

    context={
        'meu_carrinho': meu_carrinho,
        'produtos_do_carrinho': items_do_carrinho,
        'total_compra':total_compra,
        'tamanho_selecionado': tamanho,
    }

    return render(request, 'produtos/meu_carrinho.html', context=context)

def excluir_item(request, item_id: int):
    carrinho = CarrinhoItem.objects.filter(carrinho__user=request.user)
    total_compra = sum(item.total_item for item in carrinho)
    meu_carrinho = Carrinho.objects.filter(user=request.user).first()

    try:
        #produto = Produto.objects.get(id=produto_id)
        CarrinhoItem.objects.get(id=item_id).delete()

        # TODO: remover este DRY
        context={
            'meu_carrinho': meu_carrinho,
            'total_compra': total_compra,
            'produtos_do_carrinho': CarrinhoItem.objects.filter(carrinho=meu_carrinho),
        }        
        return render(request, 'produtos/meu_carrinho.html', context=context)

    except:
        # TODO:
        return render(request, 'produtos/meu_carrinho.html', context=context)



def remover_do_carrinho(request, produto_id: int):
    carrinho = CarrinhoItem.objects.filter(carrinho__user=request.user)
    total_compra = sum([item.total_item for item in carrinho])
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
        'total_compra':total_compra,
        'produtos_do_carrinho': CarrinhoItem.objects.filter(carrinho=meu_carrinho).order_by("-id"),
    }
    return render(request, 'produtos/meu_carrinho.html', context=context)



def calcular_total_carrinho(request):
    carrinho = CarrinhoItem.objects.filter(carrinho__user=request.user)
    total_compra = sum(item.total_item for item in carrinho)
    return render(request, 'produtos/meu_carrinho.html', {'carrinho': carrinho, 'total_compra': total_compra})


def finalizar_compra_whatsapp(request):
    meu_carrinho = Carrinho.objects.filter(user=request.user).first()
    items_carrinho = CarrinhoItem.objects.filter(carrinho=meu_carrinho).order_by("-id")
    total_compra = obter_total_carrinho(items_carrinho)

    produtos_texto = "\n".join([f"  {item.quantidade} x {item.produto.nome}* ({item.produto.descricao}) - Tamanho: {item.produto.tamanho}, Preço R${item.produto.valor}," for item in items_carrinho])

    texto_final = "Olá!\nGostaria de finalizar a compra. Aqui está a lista de produtos que quero adquirir:\n"
    texto_final += produtos_texto
    texto_final += f"\nTotal da compra: R${total_compra}\n" 

    tamanho_da_camiseta = request.POST.get('Rezinho_Imports')
    texto_final += f"\n REZINHO IMPORTS!{tamanho_da_camiseta}"

    return redirect(f"https://wa.me/3191235709?text={texto_final}")






