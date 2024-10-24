from django.contrib import admin
from django.urls import path,include
from escola.views import EstudanteViewSet,CursoViewSet,MatriculaViewSet, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudantes',EstudanteViewSet,basename='Estudantes')
router.register('cursos',CursoViewSet,basename='Cursos')
router.register('matriculas',MatriculaViewSet,basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('estudantes/<int:pk>/matriculas/',ListaMatriculasEstudanteSerializer.as_view()),
    path('cursos/<int:pk>/matriculas/',ListaMatriculasCursoSerializer.as_view())
]