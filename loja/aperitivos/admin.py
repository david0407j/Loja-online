
from django.contrib.admin import ModelAdmin, register

from loja.aperitivos.models import  Produto


@register(Produto)
class ProdutoAdmin(ModelAdmin):
    pass


