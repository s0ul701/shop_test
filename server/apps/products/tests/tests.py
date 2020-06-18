from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import ProductFactory
from apps.users.tests.factories import UserFactory
from apps.users.viewsets import ProtectedTokenObtainPairView


class ProductTests(APITestCase):
    """Test for Product API"""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        ProtectedTokenObtainPairView.throttle_classes = ()
        cls.url = reverse('api_v1:products-list')
        cls.product_creation_data = {
            'title': 'test_title',
            'description': 'test_description',
            'quantity': 100,
            'price': 1000,
            'image': '',
        }
        cls.product_update_data = {
            'title': 'new_test_title',
            'description': 'new_test_description',
            'quantity': 999,
            'price': 9999999,
        }
        cls.required_fields = ('title', 'description', 'quantity', 'price')

    def create_and_authenticate_admin(self):
        """Create and authenticate User by setting JWT"""
        password = 'password'
        username = 'username'
        UserFactory.create(username=username, password=password, is_staff=True)
        access_token = self.client.post(
            reverse('api_v1:token_obtain_pair'),
            data={'username': username, 'password': password}
        ).data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {access_token}')

    def test_product_retreive(self, *args, **kwargs):
        """Test Product retreive method"""
        product = ProductFactory.create()
        response = self.client.get(f'{self.url}{product.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_list(self, *args, **kwargs):
        """Test Product list method"""
        ProductFactory.create_batch(20)
        response = self.client.get(f'{self.url}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_creation(self, *args, **kwargs):
        """Test Product creation method"""
        self.create_and_authenticate_admin()
        response = self.client.post(self.url, data=self.product_creation_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_product_creation_missing_fields(self, *args, **kwargs):
        """Test Product creation method for missing fields"""
        self.create_and_authenticate_admin()
        for field in self.product_creation_data:
            with self.subTest(field=field):
                dict_with_missing_field = self.product_creation_data.copy()
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

    def test_product_update(self, *args, **kwargs):
        """Test Product update method"""
        self.create_and_authenticate_admin()
        product = ProductFactory.create()
        for field, value in self.product_creation_data.items():
            with self.subTest(field=field, value=value):
                response = self.client.patch(
                    f'{self.url}{product.id}/',
                    data={field: value}
                )
                self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_anon_update(self, *args, **kwargs):
        """Test if Anon user can`t update Product info"""
        product = ProductFactory.create()
        for field, value in self.product_update_data.items():
            with self.subTest(field=field, value=value):
                response = self.client.patch(
                    f'{self.url}{product.id}/',
                    data={field: value}
                )
                self.assertEqual(
                    response.status_code,
                    status.HTTP_401_UNAUTHORIZED
                )

    def test_product_delete(self, *args, **kwargs):
        """Test Product delete method"""
        product = ProductFactory.create()
        self.create_and_authenticate_admin()
        response = self.client.delete(f'{self.url}{product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_product_anon_delete(self, *args, **kwargs):
        """Test Anon user can`t delete Product profile"""
        product = ProductFactory.create()
        response = self.client.delete(f'{self.url}{product.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
