from django.contrib import admin
from client_hotel_reservation.models.bookings_model import Booking
from client_hotel_reservation.models.hotels_model import Hotel
from client_hotel_reservation.models.rooms_model import Room

admin.site.register(Booking)
admin.site.register(Hotel)
admin.site.register(Room)
