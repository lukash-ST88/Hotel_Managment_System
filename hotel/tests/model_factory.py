import tempfile

import factory
from django.core.files.uploadedfile import SimpleUploadedFile
from faker import Faker

from django.contrib.auth.models import User

from hotel.models import Category, Room, Booking

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'lukash'
    password = 'fylhtq03'
    email = 'email@mail.ru'
    is_staff = True


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'cat1'
    description = fake.text()
    slug = 'cat1slug'
    image = tempfile.NamedTemporaryFile(suffix=".jpg").name


class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room

    number = 100
    beds = 2
    capacity = 4
    cat = factory.SubFactory(CategoryFactory)


class BookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Booking

    check_in = fake.date_time_this_decade()
    check_out = fake.date_time_this_decade()
    user = factory.SubFactory(UserFactory)
    room = factory.SubFactory(RoomFactory)
