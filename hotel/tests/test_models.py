from hotel.models import Booking


def test_new_category(db, new_category):
    print(new_category)
    assert new_category.name == 'cat1'


def test_new_room(db, new_room):
    print(new_room)
    assert new_room.number == 100


def test_new_booking(db, new_booking):
    print(new_booking)
    assert new_booking.pk == 1


def test_room_str(db, new_room):
    assert new_room.__str__() == f'[{new_room.number}] {new_room.cat} room with {new_room.beds} bed(s) for {new_room.capacity} people'


def test_booking_str(db, new_booking):
    assert new_booking.__str__() == f'{new_booking.user} has booked {new_booking.room} from {new_booking.check_in} to {new_booking.check_out}'


def test_category_str(db, new_category):
    assert new_category.__str__() == f'{new_category.name} room'


def test_get_cancel_booking_url(db, new_booking):
    print(new_booking.get_cancel_booking_url())
    assert new_booking.get_cancel_booking_url() == '/booking/cancel/' + str(new_booking.pk)


def test_category_get_absolute_url(db, new_category):
    assert new_category.get_absolute_url() == '/room/' + str(new_category.slug)
