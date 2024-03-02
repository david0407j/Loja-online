from django.shortcuts import render
from loja.modelos.models import Categoria


def infantil(request, slug):
    infantil = Categoria.objects.all()
    return render(request, 'modelos/infantil.html', context={'infantil': infantil})
