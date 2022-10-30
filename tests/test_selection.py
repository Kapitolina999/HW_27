import json

import pytest

from ads.serializers.selection_serializers import SelectionSerializer


@pytest.mark.django_db
def test_selection_create(api_client, selection):
    data = {"name": selection.name,
            "owner": selection.owner.id,
            "items": selection.items.name}

    expected_response = SelectionSerializer(selection).data
    response = api_client.post('/selection/create/', data=json.dumps(data), content_type='application/json')
    response_data = response.json()
    assert response.status_code == 201
    assert response_data['name'] == expected_response['name']
    assert response_data['owner'] == expected_response['owner']
    assert response_data['items'] == expected_response['items']