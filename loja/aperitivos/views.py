from django.shortcuts import render

def masculino(request, slug):
    render(request, 'aperitivos/masculino.html')
