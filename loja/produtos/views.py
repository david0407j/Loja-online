from django.shortcuts import render
from loja.produtos.models import Variedade

def outros(request, nome):
    variedade = Variedade.objects.all()
    return render(request, 'produtos/outros.html', context={'variedade': variedade})
