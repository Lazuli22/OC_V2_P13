from django.contrib import admin

from .models import Letting
from .models import Adresses
from .models import Profile


admin.site.register(Letting)
admin.site.register(Adresses)
admin.site.register(Profile)
