import factory
from factory.faker import faker
from factory.fuzzy import FuzzyDecimal, FuzzyInteger
from faker.providers import internet, lorem

from apps.products.models import Product

fake = faker.Faker(locale='en_US')
fake.add_provider(internet)
fake.add_provider(lorem)


class ProductFactory(factory.django.DjangoModelFactory):
    """Factory for Product"""
    class Meta:
        model = Product

    title = factory.Sequence(lambda n: fake.text(max_nb_chars=70))
    description = factory.Sequence(lambda n: fake.text(max_nb_chars=200))
    quantity = FuzzyInteger(0, 10000)
    price = FuzzyDecimal(10, 10000)
    image = factory.Sequence(lambda n: fake.image_url())
