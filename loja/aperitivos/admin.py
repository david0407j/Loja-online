
from django.contrib.admin import ModelAdmin, register

from loja.aperitivos.models import Masculino


@register(Masculino)
class MasculinoAdmin(ModelAdmin):


    pass  
