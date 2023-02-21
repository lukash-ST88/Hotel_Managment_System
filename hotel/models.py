from django.db import models
from django.conf import settings
from django.urls import reverse, reverse_lazy


class Room(models.Model):
    number = models.IntegerField(verbose_name='Room number')
    beds = models.IntegerField(verbose_name='The quatity of beds')
    capacity = models.IntegerField(verbose_name="The room's capacity")
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, verbose_name='Category')

    def __str__(self):
        return f'[{self.number}] {self.cat} room with {self.beds} bed(s) for {self.capacity} people'


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Guest')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Room')
    check_in = models.DateTimeField(verbose_name='Check in')
    check_out = models.DateTimeField(verbose_name='Check out')

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'


    def get_cancel_booking_url(self):
        return reverse_lazy('cancel', kwargs={'pk': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="The room's category")
    description = models.TextField(verbose_name='Description')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')
    image = models.ImageField(upload_to='hotel/category/', verbose_name="The room's photo")

    def __str__(self):
        return f'{self.name} room'

    def get_absolute_url(self):
        return reverse('room', kwargs={'category': self.slug})
