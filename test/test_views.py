
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from .models import User, Profile, Post, Comment, Experience, Education
from .serializers import UserSerializer, ProfileSerializer, PostSerializer, CommentSerializer

class UserViewTest(APITestCase):
    def test_user_registration(self):
        url = reverse('user-register')  # Update with the correct url name
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)

class GetAuthUserViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_user_retrieve(self):
        url = reverse('auth-user')  # Update with the correct url name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'test@example.com')

    def test_user_login(self):
        url = reverse('user-login')  # Update with the correct url name
        data = {
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)


