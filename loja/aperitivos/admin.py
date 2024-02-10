
from django.contrib.admin import ModelAdmin, register

from loja.aperitivos.models import produtos


@register(produtos)
class produtosAdmin(ModelAdmin):
    pass