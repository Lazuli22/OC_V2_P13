import pytest
from django.test import Client
from lettings.models import Addresses, Letting


@pytest.fixture
def client_lettings():
    une_adresse = Addresses.objects.create(
        number=4, street="Military Street", city="Willoughby", state="OH",
        zip_code=44094, country_iso_code="USA")
    Letting.objects.create(title="Oceanview Retreat", Addresses_id=une_adresse.id)
    adresse_deux = Addresses.objects.create(
        number=588, street="Argyle Avenue", city="East Meadow", state="NY",
        zip_code=11554, country_iso_code="USA")
    Letting.objects.create(title="Underground Hygge", Addresses_id=adresse_deux.id)
    return Client()
