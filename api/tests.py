from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase


class TestCreateKudos(APITestCase):
    def test_should_not_create_kudo_without_auth(self):
        sample_kudo = {'title': "test_case", 'department': '1', 'team': '1', 'employee': '2'}
        response = self.client.post(reverse('create_kudo'), sample_kudo)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestUserFlow(APITestCase):
    def authenticate(self):
        self.client.post(reverse("auth_register"), {
                         "email": "amirtest5@gmail.com", "password": "123456QAws"})
        response = self.client.post(reverse("token_obtain_pair"), {
                         'email': "amirtest5@gmail.com", "password": "123456QAws"})
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {response.data['access']}")

    def test_retrieves_all_todos(self):
        self.authenticate()
        response = self.client.get(reverse('create_kudo'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['results'], list)

    def test_register(self):
        response = self.client.post(reverse("auth_register"), {
            "email": "amirtest11@gmail.com", "password": "123456QAws"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
