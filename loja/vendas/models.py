from django.db import models
from django.urls import reverse
import loja.vendas.models



class Masculino(models.Model):
    produto = models.CharField(max_length=32)
    nome = models.SlugField(max_length=32)
    preco = models.CharField(max_length=32)
    creation = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(null=True)
    img = models.ImageField(upload_to='img/')
    def get_absolute_url(self):
        return reverse('vendas:masculino', args=(self.slug,))
    def __str__(self):
        return f'Camiseta:{self.produto}'
    


class Femenina(models.Model):
    produto = models.CharField(max_length=32)
    nome = models.SlugField(max_length=32)
    preco = models.CharField(max_length=32)
    creation = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(null=True)
    img = models.ImageField(upload_to='img/')
    
    def get_absolute_url(self):
        return reverse('vendas:femenino', args=(self.slug,))

    def __str__(self):
        return f'Camisete:{self.produto}'
    


class Variedade(models.Model):
    produto = models.CharField(max_length=32)
    nome = models.SlugField(max_length=32)
    preco = models.CharField(max_length=32)
    creation = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(null=True)
    img = models.ImageField(upload_to='img/')
    
    def get_absolute_url(self):
        return reverse('vendas:produtos', args=(self.slug,))

    def __str__(self):
        return f'Variedade:{self.produto}'
    




class Infantil(models.Model):
    produto = models.CharField(max_length=32)
    nome = models.SlugField(max_length=32)
    preco = models.CharField(max_length=32)
    creation = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(null=True)
    img = models.ImageField(upload_to='img/')
    
    def get_absolute_url(self):
        return reverse('vendas:infantil', args=(self.slug,))

    def __str__(self):
        return f'Camisete:{self.produto}'