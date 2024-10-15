from rest_framework import serializers

from escola.models import Estudante, Curso

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fileds = ['id','nome', 'email', 'cpf', 'data_nascimento', 'celular']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso 
        fileds = ['id', 'codigo', 'descricao', 'nivel']        