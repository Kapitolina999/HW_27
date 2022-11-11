import factory
from django.db.models.signals import m2m_changed

from ads.models import Ad, Selection, Category
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    # username = factory.Sequence(lambda n: 'test_username%s' % n)
    username = factory.Faker('name')
    email = factory.Sequence(lambda n: 'test%s@mail.ru' % n)
    password = 'testpassword'
    role = 'admin'
    age = 36
    birth_date = factory.Faker('date_object')

    class Meta:
        model = User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: 'test_cat_name_%s' % n)
    slug = factory.Sequence(lambda n: 'slug%s' % n)


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = factory.Sequence(lambda n: 'test_ad_name_%s' % n)
    author = factory.SubFactory(UserFactory)
    price = 100
    is_published = False
    category = factory.SubFactory(CategoryFactory)


class SelectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Selection

    name = 'test_name_select'
    owner = factory.SubFactory(UserFactory)
    items = factory.RelatedFactoryList(AdFactory)


