from django.shortcuts import render

def outros(request, slug):
    return render(request, 'produtos/outros.html')
