from django.db import models


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
        return f'[{self.number}] {self.capacity} with {self.beds}(s) for {self.capacity} people(human)'