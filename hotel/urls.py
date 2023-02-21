from django.urls import path
from .views import BookingListView, RoomView, room_list_view, CancelBookingView
urlpatterns = [
    path('', room_list_view, name='rooms'),
    path('booking/list/', BookingListView.as_view(), name='bookings'),
    path('room/<str:category>', RoomView.as_view(), name='room'),
    path('booking/cancel/<str:pk>', CancelBookingView.as_view(), name='cancel'),
]