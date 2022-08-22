from django.contrib.auth.models import User
from rest_framework.test import APITestCase 
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('c3po', password='123456')

    def test_authenticates_correct_credencials(self):
        """Verifies authentication with correct credentials"""
        user = authenticate(username='c3po', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_unauthorized_request(self):
        """Non authenticated user"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_authenticates_incorrect_username(self):
        """Verifies authentication with incorrect username credentials"""
        user = authenticate(username='cpo', password='123456')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_authenticated_get_request(self):
        """"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)