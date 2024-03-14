
from django.contrib import admin 

from loja.aperitivos.models import Carrinho, Categoria, Produto



admin.site.register(Produto)

admin.site.register(Categoria)

admin.site.register(Carrinho)

