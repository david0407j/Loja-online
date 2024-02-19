from django.shortcuts import render
from loja.aperitivos.models import Masculino


def masculino(request, nome):
    masculinos = Masculino.objects.all()
    return render(request, 'aperitivos/masculino.html', context={'masculinos': masculinos})
