
from django.contrib import admin 

from loja.produtos.models import Carrinho, Categoria, Produto, Tamanho


admin.site.register(Tamanho)
admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Carrinho)

