import factory

from apps.invoices.models import Invoice
from apps.users.tests.factories import UserFactory


class InvoiceFactory(factory.django.DjangoModelFactory):
    """Factory for Invoice"""
    class Meta:
        model = Invoice

    customer = factory.SubFactory(UserFactory)
