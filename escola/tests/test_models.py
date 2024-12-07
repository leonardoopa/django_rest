from django.test import TestCase
from escola.models import Estudante

class ModelEstudanteTestCase(TestCase):
    # def test_falha_cpf_invalido(self):
    #     self.fail('Teste falhou :(')
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Joao',
            email = 'RZL6w@example.com',
            cpf = '12345678901',
            data_nascimento = '2000-01-01',
            celular = '11999999999'
        )
        