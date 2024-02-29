from django.shortcuts import render
from loja.vendas.models import Femenina
from loja.vendas.models import Variedade
from loja.vendas.models import Infantil, Masculino



def masculino(request, nome):
    masculinos = Masculino.objects.all()
    return render(request, 'vendas/masculino.html', context={'masculinos': masculinos})



def femenina(request, nome):
    femenina = Femenina.objects.all()
    return render(request, 'vendas/femenina.html', context={'femenina': femenina})



def produtos(request, nome):
    variedade = Variedade.objects.all()
    return render(request, 'vendas/produtos.html', context={'variedade': variedade})



def infantil(request, nome):
    infantil = Infantil.objects.all()
    return render(request, 'vendas/infantil.html', context={'infantil': infantil})
