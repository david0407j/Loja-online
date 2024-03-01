from django.db import models
from django.urls import reverse




class Produto(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    price = models.CharField(max_length=32)
    creation = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='img/')
    def get_absolute_url(self):
        return reverse('aperitivos:masculino', args=(self.slug,))
    def __str__(self):
        return f'Time:{self.name}'



class Categoria(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    valor = models.CharField(max_length=32)
    creation = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='img/')
    def get_absolute_url(self):
        return reverse('aperitivos:femenino', args=(self.slug,))
    def __str__(self):
        return f'Time:{self.name}'