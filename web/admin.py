from django.contrib import admin
from .models import Turma, Disciplina, Professor, Equalizacao


class Turmas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'curso')
    list_display_links = ('id', 'nome', 'curso')
    search_fields = ('nome',)
    list_display_links = ('nome', 'curso')
    list_filter = ('nome',)


admin.site.register(Turma, Turmas)


class Disciplinas(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nome', 'carga_horaria')


admin.site.register(Disciplina, Disciplinas)
admin.site.register(Professor)
admin.site.register(Equalizacao)
# Register your models here.
