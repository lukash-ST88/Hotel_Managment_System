from django.contrib import admin
from .models import Room, Booking, Category

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Category)

#TODO: добавить rest_framework
#TODO: добавить тесты
#TODO: рефактор html
#TODO: разобраться с аутентификацией allauth