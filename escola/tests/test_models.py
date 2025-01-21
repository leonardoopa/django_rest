from django.test import TestCase
from escola.models import Curso, Estudante, Matricula

class ModelEstudanteTestCase(TestCase):
    # def test_falha_cpf_invalido(self):
    #     self.fail('Teste falhou :(')
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'testedemodelo@gmail.com',
            cpf = '12345678901',
            data_nascimento = '2000-01-01',
            celular = '11999999999'
        )

    def test_verifica_atributos_de_estudante(self):
        """Teste para verificar os atributos de estudante"""
        self.assertEqual(self.estudante.nome, 'Teste de Modelo') 
        self.assertEqual(self.estudante.email, 'testedemodelo@gmail.com')
        self.assertEqual(self.estudante.cpf, '12345678901')
        self.assertEqual(self.estudante.data_nascimento, '2000-01-01')
        self.assertEqual(self.estudante.celular, '11999999999')   


class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'CTM',
            descricao = 'Curso de Teste de Modelo',
            nivel = 'B'
        )        

    def test_verifica_atributos_de_curso(self):
        """Teste para verificar os atributos de curso"""
        self.assertEqual(self.curso.codigo, 'CTM')
        self.assertEqual(self.curso.descricao, 'Curso de Teste de Modelo')
        self.assertEqual(self.curso.nivel, 'B')


class ModeloMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'testedemodelo@gmail.com',
            cpf = '12345678901',
            data_nascimento = '2000-01-01',
            celular = '11999999999' 
        ) 

        self.curso = Curso.objects.create(
            codigo = 'CTM',
            descricao = 'Curso de Teste de Modelo',
            nivel = 'B'
        )
        
        self.matricula = Matricula.objects.create(
            estudante = self.estudante,
            curso = self.curso,
            periodo = 'M'
        )

        