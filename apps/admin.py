from django.contrib import admin

# Register your models here.

from .models import Delays
from .models import Airline


admin.site.register(Delays)
admin.site.register(Airline)
