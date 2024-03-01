from django.shortcuts import render
from loja.modelos.models import Femenina


def femenina(request, slug):
    femenina = Femenina.objects.all()
    return render(request, 'modelos/femenina.html', context={'femenina': femenina})
