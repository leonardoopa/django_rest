from rest_framework import serializers

from escola.models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, celular_invalido  
class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fileds = ['id','nome', 'email', 'cpf', 'data_nascimento', 'celular']


    def validate(self, dados):
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'CPF': 'Deve ter um valor valido'})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'Nome': 'Nome só pode ter letras'})
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'Celular': 'Celular precisa seguir o padrao 86 99999-9999'})   
        
        return dados 
    
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso 
        fileds = ['id', 'codigo', 'descricao', 'nivel']       

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []            

class ListaMatriculasSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source = 'curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula 
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    def get_periodo(self,obj):
        return obj.get_periodo_display()
