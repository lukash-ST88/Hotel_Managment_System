import django.apps
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Room, Booking, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_image']

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' height=auto width=75>")

    get_image.short_description = 'Image'


class RoomAdmin(admin.ModelAdmin):
    list_display = ['number', 'beds', 'capacity', 'cat']
    list_filter = ['cat']


class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_room_num', 'check_in', 'check_out']
    list_filter = ['check_in', 'check_out']

    def get_room_num(self, obj):
        return obj.room.number

    get_room_num.short_description = 'Room'


admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Hotel ST-88'
admin.site.site_header = 'Hotel'

# TODO: настроить booking room и user в тестах
# TODO: рефактор html
# TODO: добавить ограничения по этажам

