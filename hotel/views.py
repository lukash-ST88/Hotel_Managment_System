from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, View, DeleteView
from .models import Room, Booking, Category
from .forms import AvailabilityForm
from .booking_functions.availability import check_availability
from allauth.account.views import LoginView


class RoomCategoryListView(ListView):
    model = Category
    template_name = 'hotel/rooms.html'
    context_object_name = 'room_cats'


class BookingListView(ListView):
    """A list of bookings for the staff and clients"""
    template_name = "hotel/booking_list.html"
    context_object_name = 'bookings'

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all().select_related('room')
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user).select_related('room')
            return booking_list


class RoomView(View):
    """Booking of a room"""

    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = AvailabilityForm()
        room_list = Room.objects.filter(cat__slug=category)
        if len(room_list) > 0:
            room = room_list[0]
            context = {
                'room': room,
                'form': form,
            }
            return render(request, 'hotel/room.html', context)
        else:
            return HttpResponse('Sorry! This category does not exist!')

    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        room_list = Room.objects.filter(cat__slug=category)
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse(
                'Sorry! All rooms of this kind of category is booked! Please, choose another room.')


class CancelBookingView(DeleteView):
    """Canceling of a booking"""
    model = Booking
    template_name = 'hotel/cancel_booking.html'
    success_url = reverse_lazy('bookings')
    context_object_name = 'booking'


def logout_user(request):
    logout(request)
    return redirect('rooms')



