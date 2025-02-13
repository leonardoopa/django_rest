from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

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


    def test_requisicao_get_para_listar_um_estudantes(self):
        """Teste para verificar a requisição GET para um estudante"""
        response = self.client.get(self.url + '/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)     
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(instance=dados_estudante).data
        self.assertEqual(response.data, dados_estudante_serializados)
        
    def test_requisicao_post_para_criar_um_estudante(self):
        """Teste para verificar a requisição POST para um estudante"""
        dados = {
            'nome': 'Teste de Modelo',
            'email': 'testedemodelo@gmail.com',
            'cpf': '65465765874',
            'data_nascimento': '2000-01-01',
        }
        response = self.client.post(self.url, dados) 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_requisicao_delete_um_estudante(self):    
        """Teste para verificar a requisição DELETE para um estudante"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



    def test_requisicao_put_para_atualizar_um_estudante(self):
        """Teste para verificar a requisição PUT para um estudante"""    
        dados = {
            'nome': 'Teste de Modelo put',
            'email': 'testedsddemodelo@gmail.com',
            'cpf': '65465765885',
            'data_nascimento': '2001-01-01',
            'celular': '11 99999-9999'
        }    
        response = self.client.put(f'{self.url}1/', dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
