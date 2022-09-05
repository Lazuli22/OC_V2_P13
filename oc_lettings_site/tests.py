from django.urls import reverse


def test_index_url(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


def test_index_view(client):
    url = reverse('index')
    response = client.get(url)
    assert b"Welcome to Holiday Homes" in response.content
    assert b"Profiles" in response.content
    assert b'Lettings' in response.content
