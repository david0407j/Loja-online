from django.shortcuts import render, redirect

from loja.produtos.models import Carrinho, CarrinhoItem, Categoria, Produto
from loja.produtos.service import carrinho


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
    meu_carrinho = carrinho.obter_carrinho(request.user)
    return render(request, 'produtos/meu_carrinho.html', context=meu_carrinho)


def adicionar_no_carrinho(request, produto_id: int):
    quantidade = 1
    tamanho = request.POST.get('tamanho')
    carrinho.adicionar_item(request.user, produto_id, quantidade, tamanho)

    meu_carrinho = carrinho.obter_carrinho(request.user)
    meu_carrinho['tamanho_selecionado'] = tamanho
    return render(request, 'produtos/meu_carrinho.html', context=meu_carrinho)


def excluir_item(request, item_id: int):
    meu_carrinho = carrinho.excluir_item(request.user, item_id)
    return render(request, 'produtos/meu_carrinho.html', context=meu_carrinho)


def remover_do_carrinho(request, produto_id: int):
    quantidade = 1
    tamanho = None
    item, meu_carrinho = carrinho.remover_item(request.user, produto_id, quantidade, tamanho)
    return render(request, 'produtos/meu_carrinho.html', context=meu_carrinho)


def finalizar_compra_whatsapp(request):
    meu_carrinho = carrinho.obter_carrinho(request.user)
    items_carrinho = meu_carrinho['produtos_do_carrinho']
    total_compra = meu_carrinho['total_compra']

    produtos_texto = "\n".join([f"  {item.quantidade} x {item.produto.nome}* ({item.produto.descricao}) - Tamanho: {item.produto.tamanho}, Preço R${item.produto.valor}," for item in items_carrinho])

    texto_final = "Olá!\nGostaria de finalizar a compra. Aqui está a lista de produtos que quero adquirir:\n"
    texto_final += produtos_texto
    texto_final += f"\nTotal da compra: R${total_compra}\n" 

    tamanho_da_camiseta = request.POST.get('Rezinho_Imports')
    texto_final += f"\n REZINHO IMPORTS!{tamanho_da_camiseta}"

    return redirect(f"https://wa.me/3191235709?text={texto_final}")
