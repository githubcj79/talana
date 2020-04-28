from django.contrib import admin

# Register your models here.

from .models import Car, CarInstance

admin.site.register(Car)
admin.site.register(CarInstance)
