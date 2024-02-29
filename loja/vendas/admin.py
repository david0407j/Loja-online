
from django.contrib.admin import ModelAdmin, register
from loja.vendas.models import Masculino, Infantil
from loja.vendas.models import  Variedade
from loja.vendas.models import Femenina


@register(Masculino)
class MasculinoAdmin(ModelAdmin):
    pass  



@register(Femenina)
class FemeninaAdmin(ModelAdmin):
    pass



@register(Variedade)
class VariedadeAdmin(ModelAdmin):
    pass


@register(Infantil)
class InfantilAdmin(ModelAdmin):
    pass


