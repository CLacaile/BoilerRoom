from django.contrib import admin

from .models import Room, Sensor, Measure

admin.site.register(Room)
admin.site.register(Sensor)
admin.site.register(Measure)
