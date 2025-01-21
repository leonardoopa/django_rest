from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class MatriculaTestCase(APITestCase):
    def setup (self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        url = reverse('Estudante-list')
        self.client.force_authenticate(self.usuario)
        
