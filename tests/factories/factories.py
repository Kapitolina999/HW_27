import factory

from ads.models import Ad, Selection
from users.models import Location, User


class UserFactory(factory.django.DjangoModelFactory):
    username = 'test_name_'
    email = 'test@test.ru'
    password = 'testpassword'
    role = 'admin'
    age = 36
    birth_date = factory.Faker('date_object')

    class Meta:
        model = User


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = 'test_name_'
    author = factory.SubFactory(UserFactory)
    price = 100
    is_published = False


class LocationFactory(factory.django.DjangoModelFactory):
    name = 'test_name'
    lat = 1.111111
    lng = 1.111111

    class Meta:
        model = Location

# class SelectionFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Selection
#
#     name = 'test_name'
#     owner = factory.SubFactory(UserFactory)