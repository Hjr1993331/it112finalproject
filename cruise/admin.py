from django.contrib import admin
from .models import TravelType, Trip, Questions
# Register your models here.

admin.site.register(TravelType)
admin.site.register(Trip)
admin.site.register(Questions)