from allauth.account import signals
from django.urls import reverse
from datetime import datetime


def test_booking_list_GET_for_staff(client, db, new_user):
    logged_in = client.post(reverse("account_login"), data={"login": "user", "password": "fylhtq03"})
    print(logged_in.context['user'])
    print(new_user.username)
    assert logged_in.status_code == 200


def test_room_detail_GET_free_room(client, new_room):
    response = client.get(reverse('room', args=[new_room.cat.slug]))
    # print(response.content)
    assert response.status_code == 200


def test_room_detail_GET_no_free_rooms(client, new_room):
    response = client.get(reverse('room', args=['booked-room']))
    # print(response.content)
    assert response.status_code == 200
    assert response.content == b'Sorry! This category does not exist!'

# def test_room_detail_POST_free_room(client, new_room, new_user):
#     response = client.post(reverse('room', args=[new_room.cat.slug]), data={
#         'user': new_user,
#         'room': new_room,
#         'check_in': datetime(2023, 1, 1, 12, 0, 0),
#         'check_out': datetime(2023, 1, 2, 12, 0, 0),
#     })
#     print(response.status_code)
#     assert response.status_code == 302
