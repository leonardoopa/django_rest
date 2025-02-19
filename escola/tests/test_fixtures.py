from django.test import TestCase
from escola.models import Estudante, Curso


class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_carregamento_da_fixtures(self):
        """"Teste para verificar o carregamento da fixtures"""
        estudante = Estudante.objects.get(cpf= '72165846541')
        curso = Curso.objects.get(pk=1)
        self.assertEqual(estudante.celular, '11 99999-9999')
        self.assertEqual(curso.descricao, 'Curso teste 1')
