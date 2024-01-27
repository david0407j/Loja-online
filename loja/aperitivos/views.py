from django.shortcuts import render

def masculino(request, slug):
    return render(request, 'aperitivos/masculino.html')


