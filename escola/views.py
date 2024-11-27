from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer, MatriculaSerializer
from rest_framework import viewsets, generics, filters
from rest_framework import serializers  
from django_filters.rest_framework import DjangoFilterBackend

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all().order_by("id")
    serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['nome']
    searched_fields = ['nome', 'cpf', 'celular']

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['curso']


class MatriculaViewSet(viewsets.ModelViewSet): 
    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer    
    


class ListaMatriculas(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id = self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculasEstudanteView(generics.ListAPIView):
    serializer_class = ListaMatriculasEstudanteSerializer

    def get_queryset(self):
        return Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by("id")
    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    def get_periodo(self,obj):
        return obj.get_periodo_display()

class ListaMatriculasCursoView(generics.ListAPIView):
    serializer_class = ListaMatriculasCursoSerializer

    def get_queryset(self):
        return Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by("id")
    class Meta:
        model = Matricula
        fields = ['estudante_nome']