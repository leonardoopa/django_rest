from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from rest_framework import status

class AuthenticationTest(APITestCase):
    def setup (self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        url = reverse('Estudante-list')

    def test_authenticate(self):
        """ Test que verifica a autenticação de usuário """ 
        usuario = authenticate(username='admin', password='admin')
        self.assertFalse(usuario is not None) and usuario.is_authenticated

    def test_authenticate_com_informacoes_incorretas(self):
        """ Test que verifica a autenticação de usuário incorretas""" 
        usuario = authenticate(username='admin', password='admin')
        self.assertFalse(usuario is not None) and usuario.is_authenticated


    def test_authenticate_com_senha_errada(self):
        """ Test que verifica a autenticação de senha errada""" 
        usuario = authenticate(username='admin', password='adm')
        self.assertFalse(usuario is not None) and usuario.is_authenticated

    def test_requisicao_get_autorizada(self):
        """ Test que verifica uma requisiçao GET autorizada""" 
        self.client.force_authenticate(self.usuario)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



        