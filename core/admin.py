from django.contrib import admin

from .models import Inicio


@admin.register(Inicio)
class InicioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'profissao1', 'profissao2', 'github', 'linkedin', 'facebook',
                    'descricao', 'nacionalidade', 'cidade_estado', 'email', 'telefone')
