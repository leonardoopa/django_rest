from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from escola.models import Estudante

class EsudantesTestCase(APITestCase):
    def setup (self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        url = reverse('Estudante-list')
        self.client.force_authenticate(self.usuario)
        self.estudante_01 = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'testedemodelo@gmail.com',
            cpf = '72165846541',
            data_nascimento = '2000-01-01',
            
            celular = '11 99999-9999'
        )
        self.estudante_02 = Estudante.objects.create(
            nome = 'Teste de Modelo 2',
            email = 'testedemodelo2@gmail.com',
            cpf = '72165526541',
            data_nascimento = '2000-01-01',
            celular = '81 99999-9999'
        )


    def test_requisicao_get_para_listar_estudantes(self):
        """Teste para verificar a requisição GET para listagem de estudantes"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

        
