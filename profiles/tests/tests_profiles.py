from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_profiles_url(client_profiles):
    url = reverse('profiles_index')
    response = client_profiles.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_profiles_view(client_profiles):
    url = reverse('profiles_index')
    response = client_profiles.get(url)
    assert b"Profiles" in response.content
    assert b"AirWow" in response.content
