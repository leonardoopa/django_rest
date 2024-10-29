from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer, MatriculaSerializer
from rest_framework import viewsets, generics
from rest_framework import serializers  

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet): 
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer    


class ListaMatriculas(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculasEstudanteView(generics.ListAPIView):
    serializer_class = ListaMatriculasEstudanteSerializer

    def get_queryset(self):
        return Matricula.objects.filter(estudante_id=self.kwargs['pk'])    
    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    def get_periodo(self,obj):
        return obj.get_periodo_display()

class ListaMatriculasCursoView(generics.ListAPIView):
    serializer_class = ListaMatriculasCursoSerializer

    def get_queryset(self):
        return Matricula.objects.filter(curso_id=self.kwargs['pk'])
    class Meta:
        model = Matricula
        fields = ['estudante_nome']