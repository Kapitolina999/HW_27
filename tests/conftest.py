import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from factories.factories import UserFactory, AdFactory, CategoryFactory, SelectionFactory

register(AdFactory)
register(UserFactory)
register(CategoryFactory)
register(SelectionFactory)


@pytest.fixture
def api_client(db, user):
    client = APIClient()
    token = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')
    return client


