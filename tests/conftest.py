import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from factories.factories import UserFactory, LocationFactory, AdFactory

register(AdFactory)
register(UserFactory)
register(LocationFactory)


@pytest.fixture
@pytest.mark.django_db
def access_token(client, user):

    response = client.post('/user/token/', {'username': user.username, 'password': user.password}, format='json')
    print(response)
    print(response.data)
    return response.data["access_token"]


# @pytest.fixture
# def api_client(db, user):
#     client = APIClient()
#     token = RefreshToken.for_user(user)
#     client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')
#     return client
