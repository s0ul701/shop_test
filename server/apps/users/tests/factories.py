import factory
from django.contrib.auth.models import User
from factory.faker import faker
from faker.providers import internet, person

fake = faker.Faker(locale='en_US')
fake.add_provider(internet)
fake.add_provider(person)


class UserFactory(factory.django.DjangoModelFactory):
    """Factory for User"""
    class Meta:
        model = User

    email = factory.Sequence(lambda n: fake.email())
    first_name = factory.Sequence(lambda n: fake.first_name())
    last_name = factory.Sequence(lambda n: fake.last_name())
    username = factory.LazyAttribute(lambda user: f'{user.first_name}_{user.last_name}')
    password = factory.PostGenerationMethodCall('set_password', 'password')
