import factory
from factory.fuzzy import FuzzyDecimal, FuzzyInteger

from .invoice import InvoiceFactory
from apps.invoices.models import InvoicePosition
from apps.products.tests.factories import ProductFactory


class InvoicePositionFactory(factory.django.DjangoModelFactory):
    """Factory for Invoice Position"""
    class Meta:
        model = InvoicePosition

    invoice = factory.SubFactory(InvoiceFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = FuzzyInteger(0, 10000)
    price = FuzzyDecimal(10, 10000)
