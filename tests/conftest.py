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
    client.post('/user/create/', {'username': user.username, 'email': user.email, 'password': user.password,
                                  'role': user.role, 'age': user.age, 'birth_date': user.birth_date,
                                  'location': user.location}, format='json')

    response = client.post('/user/token/', {'username': user.username, 'password': user.password}, format='json')

    return response.data["access"]


# @pytest.fixture
# def api_client(db, user):
#     client = APIClient()
#     token = RefreshToken.for_user(user)
#     client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')
#     return client
