from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, View, DeleteView
from .models import Room, Booking
from .forms import AvailabilityForm
from .booking_functions.availability import check_availability


def room_list_view(request):
    """список всех категорий номеров"""
    room = Room.objects.all()[0]
    room_categories = dict(room.ROOM_CATS)
    room_list = []
    for room_cat_short, room_cat_full in room_categories.items():
        room_url = reverse('room', kwargs={'category': room_cat_short})
        room_list.append((room_cat_full, room_url))
    context = {"room_list": room_list}
    return render(request, 'hotel/room_list.html', context)


class BookingListView(ListView):
    """список бронирований номеров для сотрудников и клиентов"""
    template_name = "hotel/booking_list.html"
    context_object_name = 'bookings'

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list


class RoomView(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = AvailabilityForm()
        room_list = Room.objects.filter(category=category)

        if len(room_list) > 0:
            room = room_list[0]
            room_category = dict(room.ROOM_CATS).get(room.category, None)
            context = {
                'room_category': room_category,
                'form': form,
            }
            return render(request, 'hotel/room.html', context)
        else:
            return HttpResponse('Извините, данной категории не существует')

    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        room_list = Room.objects.filter(category=category)
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
                'Извините, все комнаты данной категории забронированы! Выберите, пожалуйста, другую категорию.')

class CancelBookingView(DeleteView):
    model = Booking
    template_name = 'hotel/cancel_booking.html'
    success_url = reverse_lazy('bookings')

