from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import InvoiceFactory, InvoicePositionFactory
from apps.users.tests.factories import UserFactory
from apps.users.viewsets import ProtectedTokenObtainPairView


class ProductTests(APITestCase):
    """Test for Product API"""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        ProtectedTokenObtainPairView.throttle_classes = ()
        cls.url = reverse('api_v1:invoices-list')

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

    def test_invoice_retreive(self, *args, **kwargs):
        """Test Invoice retreive method"""
        invoice = InvoiceFactory.create()
        InvoicePositionFactory.create_batch(10, invoice=invoice)
        self.create_and_authenticate_admin()
        response = self.client.get(f'{self.url}{invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invoice_list(self, *args, **kwargs):
        """Test Invoice list method"""
        self.create_and_authenticate_admin()
        invoices = InvoiceFactory.create_batch(20)
        [
            InvoicePositionFactory.create_batch(10, invoice=invoice)
            for invoice in invoices
        ]
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invoice_delete(self, *args, **kwargs):
        """Test Invoice delete method"""
        self.create_and_authenticate_admin()
        invoice = InvoiceFactory.create()
        InvoicePositionFactory.create_batch(10, invoice=invoice)
        response = self.client.delete(f'{self.url}{invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invoice_anon_delete(self, *args, **kwargs):
        """Test Anon user can`t delete Invoice profile"""
        invoice = InvoiceFactory.create()
        InvoicePositionFactory.create_batch(10, invoice=invoice)
        response = self.client.delete(f'{self.url}{invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
