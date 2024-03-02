
from django.contrib.admin import ModelAdmin, register

from loja.modelos.views import  Categoria


@register(Categoria)
class CategoriaAdmin(ModelAdmin):
    pass