from django.shortcuts import render

def femenina(request, slug):
    return render(request, 'modolos/femenina.html')
