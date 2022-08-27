from django.contrib import admin

from lettings.models import Letting
from lettings.models import Addresses
from .models import Profile


admin.site.register(Letting)
admin.site.register(Addresses)
admin.site.register(Profile)
