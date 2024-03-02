from django.shortcuts import render
from loja.aperitivos.models import  Produto


def masculino(request, slug):
    masculinos = Produto.objects.all()
    return render(request, 'aperitivos/masculino.html', context={'masculinos': masculinos})


