from django.shortcuts import render
from loja.aperitivos.models import  Produto


def Produto(request, slug):
    Produto = Produto.objects.all()
    return render(request, 'aperitivos/masculino.html', context={'masculinos': masculinos})


