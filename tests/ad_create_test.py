import json
from datetime import date

import pytest


# @pytest.mark.django_db
# def test_ad_create(client, ad):
#     expected_response = {
#         "id": ad.pk,
#         "name": "test_name_",
#         "author": ad.author_id,
#         "price": 100,
#         "description": '',
#         "is_published": False,
#         "image": "",
#         "category": "",
#         "created": date.today().strftime('%Y-%m-%d')
#     }
#
#     data = ad.__dict__
#     response = client.post("/ad/", data, content_type='application/json')
#
#     assert response.statuse_code == 200
#     assert response.data == expected_response
from django.http import JsonResponse


@pytest.mark.django_db
def test_location_create(client, location, access_token):
    expected_response = {
        "name": "test_name",
        "lat": 1.111111,
        "lng": 1.111111
    }

    response = client.post("/location/create/", data={"name": location.name, "lat": location.lat, "lng": location.lng},
                           content_type='application/json', HTTP_AUTHORIZATION=f'Bearer {access_token}')
    assert response.status_code == 201
    assert json.loads(response.content) == expected_response


# @pytest.mark.django_db
# def test_create_ad(api_client, user):
#     data = {
#         'name': 'test_ad_test',
#         'author': user.id,
#         'price': 10,
#         'is_published': True
#     }
#     url = reverse('ad_create')
#     res = api_client.post(url, data=json.dumps(data),
#                           content_type='application/json')
#     res_data = res.json()
#     assert res.status_code == status.HTTP_201_CREATED
#     assert res_data['name'] == data['name']
#     assert res_data['author'] == data['author']
#     assert res_data['price'] == data['price']


@pytest.mark.django_db
def test_create_ads(api_client):
    url = reverse('ad_list')
    res = api_client.get(url)
    assert res.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_ad_by_id(api_client, ad):
    url = reverse('ad_detail', kwargs={'pk': ad.id})
    res = api_client.get(url)
    assert res.status_code == status.HTTP_200_OK
    assert res.json()['id'] == ad.id