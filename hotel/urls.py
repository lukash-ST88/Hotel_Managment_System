from django.urls import path
from .views import BookingListView, RoomView, CancelBookingView, RoomCategoryListView, logout_user
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('booking/list/', BookingListView.as_view(), name='bookings'),
    path('room/<str:category>', RoomView.as_view(), name='room'),
    path('booking/cancel/<str:pk>', CancelBookingView.as_view(), name='cancel'),
    path('', cache_page(60)(RoomCategoryListView.as_view()), name='rooms'),
    path('logout/', logout_user, name='logout'),
]

