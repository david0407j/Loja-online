from django.shortcuts import render
from loja.produtos.models import Variedade


def variedade(request, nome):
    variedade = Variedade.objects.all()
    return render(request, 'produtos/variedade.html', context={'variedade': variedade})
