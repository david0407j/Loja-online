
from django.contrib.admin import ModelAdmin, register

from loja.aperitivos.models import Categoria, Produto


@register(Produto)
class ProdutoAdmin(ModelAdmin):
    pass


@register(Categoria)
class CategoriaAdmin(ModelAdmin):
    pass
