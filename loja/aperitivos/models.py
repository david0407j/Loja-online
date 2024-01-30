from django.db import models
from django.urls import reverse


class masculino(models.Model):
    titulo = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    masculino = models.CharField(max_length=32)
   
def get_absolute_url(self):
        return reverse('aperitivos:masculino', args=(self.slug,))

