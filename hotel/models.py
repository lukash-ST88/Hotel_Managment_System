from django.db import models
from  django.conf import settings

class Room(models.Model):
    ROOM_CATS = (
        ('C', 'Cheap'),
        ('N', 'Normal'),
        ('L', 'Luxury')
    )
    number = models.IntegerField()
    category = models.CharField(max_length=1, choices=ROOM_CATS)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'[{self.number}] {self.category} room with {self.beds} bed(s) for {self.capacity} people'


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'
