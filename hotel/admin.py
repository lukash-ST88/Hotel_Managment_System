from django.contrib import admin
from .models import Room, Booking, Category

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Category)


#TODO: настроить booking room и user в тестах
#TODO: рефактор html
