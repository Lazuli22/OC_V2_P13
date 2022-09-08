import pytest
from django.test import Client
from profiles.models import Profile
from django.contrib.auth.models import User 


@pytest.fixture
def client_profiles():
    un_user = User.objects.create(
        username="AirWow", first_name="Ada", last_name="Paul",
        email="flocation.vam4@glendenningflowerdesign.com")
    Profile.objects.create(favorite_city="Barcelona", user_id=un_user.id)
    return Client()
