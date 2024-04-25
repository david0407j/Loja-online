from django.contrib import admin
from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'email', 'telefone', 'celular', 'cor_favorita', 'comida_favorita')
    search_fields = ('nome', 'email')
    list_filter = ('cor_favorita', 'comida_favorita')
    ordering = ('nome',)
    fieldsets = (
        (None, {
            'fields': ('nome', 'data_nascimento', 'email', 'senha')
        }),
        ('Contato', {
            'fields': ('telefone', 'celular')
        }),
        ('Preferências', {
            'fields': ('cor_favorita', 'comida_favorita')
        }),
    )
    readonly_fields = ('senha', 'confirmar_senha') 

admin.site.register(Pessoa, PessoaAdmin)

