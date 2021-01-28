from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

test_user = {
    "username": "testnonuser",
    "email": "testnonuser@users.com",
    "password1": "strongPassword$123",
    "password2": "strongPassword$123",
}

test_profile_data = {
    "desc": "THE description \r\n of the test user is mutline",
    "colour": "pink",
}

test_other_user = {"username": "otherguyuser", "password": "goodPassword%23"}

registration_url = "/api/rest-auth/registration"


profile_list_url = reverse("profiles-list")


def profile_detail_url(pk):
    return reverse("profiles-detail", kwargs={"pk": pk})


class RegistrationTestCase(APITestCase):
    def test_registration(self):
        """a user can be registered"""
        data = test_user.copy()
        response = self.client.post(registration_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProfileViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username=test_user.get("username"), password=test_user.get("password1")
        )
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.api_authenticate_self_user()

    def api_authenticate_self_user(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_profile_list_authenticated(self):
        """only authenticated user can list all profiles"""
        response = self.client.get(profile_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_unauthenticated(self):
        """unauthenticated users cannot view all profiles'"""
        self.client.credentials()
        response = self.client.get(profile_list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_profile_retrieve_correct(self):
        """the correct user profile with details can be found"""
        response = self.client.get(profile_detail_url(1))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], test_user.get("username"))

    def test_profile_update_by_own_user(self):
        """profile can be updated by its owner
        a profile is auto created on user creation"""

        response = self.client.put(profile_detail_url(1), test_profile_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_update_by_not_owner(self):
        """profile of a user cannot be updated by other user"""
        other_user = User.objects.create_user(
            username=test_other_user.get("username"),
            password=test_other_user.get("password"),
        )
        self.client.force_authenticate(user=other_user)
        response = self.client.put(
            profile_detail_url(1),
            {"desc": "other user changed the decription of test_user"},
        )

        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)
