from django.urls import path
from .views import BookingListView, BookingView, RoomView, room_list_view
urlpatterns = [
    path('room_list/', room_list_view, name='rooms'),
    path('booking_list/', BookingListView.as_view(), name='bookings'),
    path('book/', BookingView.as_view(), name='booking_room'),
    path('room/<str:category>', RoomView.as_view(), name='room')
]