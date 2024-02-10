from django.db import models
from django.urls import reverse


class produtos(models.Model):
    produto = models.CharField(max_length=32)
    nome = models.SlugField(max_length=32)
    preco = models.CharField(max_length=32)
    creation = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField()
    
    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))

    def __str__(self):
        return f'camisa:{self.produto}'