
from django.contrib.admin import ModelAdmin, register

from loja.produtos.models import  Variedade


@register(Variedade)
class VariedadeAdmin(ModelAdmin):
    pass
  