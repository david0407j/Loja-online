
from django.contrib.admin import ModelAdmin, register

from loja.modelos.views import Femenina


@register(Femenina)
class FemeninaAdmin(ModelAdmin):
    pass