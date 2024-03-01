from django.shortcuts import render
from loja.aperitivos.models import Categoria, Produto


def masculino(request, slug):
    masculinos = Produto.objects.all()
    return render(request, 'aperitivos/masculino.html', context={'masculinos': masculinos})


def feminina(request):
    feminina = Categoria.objects.all()
    return render(request, 'aperitivos/feminina.html', context={'feminina': feminina})
