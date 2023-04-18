import pytest
from django.urls import reverse
from pytest_factoryboy import register

from model_factory import CategoryFactory, RoomFactory, UserFactory, BookingFactory

register(UserFactory)
register(CategoryFactory)
register(RoomFactory)
register(BookingFactory)


@pytest.fixture(scope='function')
def new_category(db, category_factory):
    category = category_factory.create()
    return category


@pytest.fixture(scope='function')
def new_user(db, user_factory):
    user = user_factory.create()
    return user


@pytest.fixture(scope='function')
def new_room(db, room_factory):
    room = room_factory.create()
    return room


@pytest.fixture(scope='function')
def new_booking(db, booking_factory):
    booking = booking_factory.create()
    return booking

