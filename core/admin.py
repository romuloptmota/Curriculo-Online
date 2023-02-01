from django.contrib import admin

from .models import Inicio, Formacao


@admin.register(Inicio)
class InicioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'profissao1', 'profissao2', 'github', 'linkedin', 'facebook',
                    'descricao', 'nacionalidade', 'cidade_estado', 'email', 'telefone')


@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'ano_conclusao', 'instituicao')
