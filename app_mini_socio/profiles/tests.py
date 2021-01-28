from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


test_user = {
    "username": "testnonuser",
    "email": "testnonuser@users.com",
    "password1": "strongPassword$123",
    "password2": "strongPassword$123",
}


class RegistrationTestCase(APITestCase):
    def test_registration(self):
        """test that a user can be registered"""
        data = test_user.copy()
        response = self.client.post("/api/rest-auth/registration", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
