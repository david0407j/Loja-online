from django.db import models
from django.urls import reverse


class masculino(models.Model):
    produtos = models.CharField(max_length=32)
    camisa= models.SlugField(max_length=32)
    masculino = models.CharField(max_length=32)
    creation = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('aperitivos:masculino', args=(self.slug,))

    def __str__(self):
        return f'masculino:{self.produtos}'
