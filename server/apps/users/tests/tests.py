from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import UserFactory
from apps.users.viewsets import ProtectedTokenObtainPairView, UserViewSet


class UserTests(APITestCase):
    """Test for User API"""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        UserViewSet.throttle_classes = ()
        ProtectedTokenObtainPairView.throttle_classes = ()
        cls.url = reverse('api_v1:users-list')
        cls.user_creation_data = {
            'username': 'test_username',
            'email': 'test@email.com',
            'password': 'test_password',
            'confirm_password': 'test_password',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
        }
        cls.user_update_data = {
            'username': 'new_username',
            'email': 'new@email.com',
            'first_name': 'new_first_name',
            'last_name': 'new_last_name',
        }
        cls.user_update_password = {
            'password': 'new_password',
            'confirm_password': 'new_password',
        }
        cls.required_fields = ('username', 'password', 'confirm_password')

    def authenticate_user(self):
        """Authenticate User by setting JWT"""
        access_token = self.client.post(
            reverse('api_v1:token_obtain_pair'),
            data={
                'username': self.user_creation_data['username'],
                'password': self.user_creation_data['password']
            }
        ).data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {access_token}')

    def test_user_creation(self, *args, **kwargs):
        """Test User creation method"""
        response = self.client.post(self.url, data=self.user_creation_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_creation_missing_fields(self, *args, **kwargs):
        """Test User creation method for missing fields"""
        for counter, field in enumerate(self.user_creation_data.keys()):
            with self.subTest(field=field, counter=counter):
                dict_with_missing_field = self.user_creation_data.copy()
                dict_with_missing_field['username'] += f'{counter}'
                del dict_with_missing_field[field]
                response = self.client.post(
                    self.url,
                    data=dict_with_missing_field
                )
                if field in self.required_fields:
                    self.assertEqual(
                        response.status_code,
                        status.HTTP_400_BAD_REQUEST
                    )
                else:
                    self.assertEqual(
                        response.status_code,
                        status.HTTP_201_CREATED
                    )

    def test_user_update(self, *args, **kwargs):
        """Test User update method"""
        user = UserFactory.create(
            username=self.user_creation_data['username'],
            password=self.user_creation_data['password']
        )
        self.authenticate_user()
        for field, value in self.user_update_data.items():
            with self.subTest(field=field, value=value):
                response = self.client.patch(
                    f'{self.url}{user.id}/',
                    data={field: value}
                )
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(
                    response.data[field], self.user_update_data[field]
                )

    def test_user_password_update(self, *args, **kwargs):
        """Test User update password method"""
        user = UserFactory.create(
            username=self.user_creation_data['username'],
            password=self.user_creation_data['password']
        )
        self.authenticate_user()
        response = self.client.patch(
            f'{self.url}{user.id}/',
            data=self.user_update_password
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_anon_update(self, *args, **kwargs):
        """Test if Anon user can`t update User info"""
        user = UserFactory.create()
        for field, value in self.user_update_data.items():
            with self.subTest(field=field, value=value):
                response = self.client.patch(
                    f'{self.url}{user.id}/',
                    data={field: value}
                )
                self.assertEqual(
                    response.status_code,
                    status.HTTP_401_UNAUTHORIZED
                )

    def test_user_delete(self, *args, **kwargs):
        """Test User delete method"""
        user = UserFactory.create(
            username=self.user_creation_data['username'],
            password=self.user_creation_data['password']
        )
        self.authenticate_user()
        response = self.client.delete(f'{self.url}{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_anon_delete(self, *args, **kwargs):
        """Test Anon user can`t delete User profile"""
        user = UserFactory.create()
        response = self.client.delete(f'{self.url}{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_retreive(self, *args, **kwargs):
        """Test User retreive method"""
        user = UserFactory.create()
        response = self.client.get(f'{self.url}{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_list(self, *args, **kwargs):
        """Test User list method"""
        UserFactory.create_batch(20)
        response = self.client.get(f'{self.url}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
