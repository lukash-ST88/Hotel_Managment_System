from django.urls import reverse, resolve
from hotel.views import BookingListView, RoomView, RoomCategoryListView, CancelBookingView, logout_user


def test_url_booking_list():
    url = reverse('bookings')
    assert resolve(url).func.view_class == BookingListView


def test_url_room_list():
    url = reverse('rooms')
    assert resolve(url).func.view_class == RoomCategoryListView


def test_url_logout_user():
    url = reverse('logout')
    assert resolve(url).func == logout_user


def test_url_cancel_booking():
    url = reverse('cancel', args=[1])
    print(dir(resolve(url).func))
    assert resolve(url).func.view_class == CancelBookingView


def test_url_room():
    url = reverse('room', args=['cat-slug'])
    assert resolve(url).func.view_class == RoomView
