from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_lettings_url(client_lettings):
    url = reverse('lettings_index')
    response = client_lettings.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_lettings_view(client_lettings):
    url = reverse('lettings_index')
    response = client_lettings.get(url)
    assert b"Lettings" in response.content
    assert b"Oceanview Retreat" in response.content
    assert b"Underground Hygge" in response.content
