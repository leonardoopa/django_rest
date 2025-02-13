from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer, MatriculaSerializer
from rest_framework import viewsets, generics, filters
from rest_framework import serializers  
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from escola.thottles import MatriculaAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class EstudanteViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de estudantes.

    Campos de ordenação:
    - nome: permite ordenar os resultados por nome.

    Campos de pesquisa:
    - nome: permite pesquisar os resultados por nome.
    - cpf: permite pesquisar os resultados por CPF.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE

    Classe de Serializer:
    - EstudanteSerializer: usado para serialização e desserialização de dados.
    - Se a versão da API for 'v2', usa EstudanteSerializerV2.
    """

    queryset = Estudante.objects.all().order_by("id")
    serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['nome']
    searched_fields = ['nome', 'cpf', 'celular']

class CursoViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de cursos.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    """
     
    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['curso']
    permission_classes = [IsAuthenticatedOrReadOnly]

class MatriculaAnonRateThrottle(MatriculaAnonRateThrottle):
    rate = '5/day'

class MatriculaViewSet(viewsets.ModelViewSet): 

    """
    Descrição da ViewSet:
    - Endpoint para CRUD de matrículas.

    Métodos HTTP Permitidos:
    - GET, POST

    Throttle Classes:
    - MatriculaAnonRateThrottle: limite de taxa para usuários anônimos.
    - UserRateThrottle: limite de taxa para usuários autenticados.
    """

    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer   
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle] 
    http_method_names = ['get', 'post']

    
class ListaMatriculas(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Estudante
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """

    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id = self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculasEstudanteView(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Estudante
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """
    serializer_class = ListaMatriculasEstudanteSerializer

    def get_queryset(self):
        return Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by("id")
    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    def get_periodo(self,obj):
        return obj.get_periodo_display()

class ListaMatriculasCursoView(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Curso
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """

    serializer_class = ListaMatriculasCursoSerializer

    def get_queryset(self):
        return Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by("id")
    class Meta:
        model = Matricula
        fields = ['estudante_nome']