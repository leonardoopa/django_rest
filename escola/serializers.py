from rest_framework import serializers

from escola.models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fileds = ['id','nome', 'email', 'cpf', 'data_nascimento', 'celular']


    def validate(self, dados):
        if len(dados['cpf']) != 11:
            raise serializers.ValidationError({'CPF': 'CPF deve conter 11 digitos'})
        if not dados['nome'].isalpha():
            raise serializers.ValidationError({'Nome': 'Nome só pode ter letras'})
        if len(dados['celular']) != 13:
            raise serializers.ValidationError({'Celular': 'Celular deve conter 13 digitos'})
        
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
