from django.contrib import admin
from .models import Room, Booking

admin.site.register(Room)
admin.site.register(Booking)

#TODO: добавить rest_framework
#TODO: сделать описание категорий и добавить модель категорий
#TODO: рефактор html