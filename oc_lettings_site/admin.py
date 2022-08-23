from django.contrib import admin

from .models import Letting
from .models import Addresses
from .models import Profile


admin.site.register(Letting)
admin.site.register(Addresses)
admin.site.register(Profile)
