from django.test import TestCase
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
# Create your tests here.
from authentication.models import Employee
from authentication.serializers import RegisterSerializer

client = Client()


class SignUpTest(TestCase):
    """ Test module for SignUp users API """

    def setUp(self):
        Employee.objects.create(
            email='amirh.moshfeghi3@gmail.com', password='123456QAws', first_name='amir3', last_name='moshfegh3')

    def test_signup(self):
        # get API response
        response = client.get(reverse('auth_register'))
        # get data from db
        emps = Employee.objects.all()
        serializer = RegisterSerializer(emps)
        print(serializer)
        print(response)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)