from django.contrib import admin
from escola.models import Estudante, Curso

class Estudantes(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'data_nascimento', 'celular', 'id')
    list_display_links = ('nome', 'id')  
    list_per_page = 20
    search_fields = ('nome', 'email', 'cpf', 'data_nascimento', 'celular')
    ordering = ('nome',)

admin.site.register(Estudante, Estudantes)

class Cursos(admin.ModelAdmin):
    list_display = ('codigo', 'descricao', 'id')
    list_display_links = ('codigo', 'id')
    search_fields = ('codigo',)
    
admin.site.register(Curso, Cursos)    

