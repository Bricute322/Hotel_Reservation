from rest_framework import serializers
from client_hotel_reservation.models.bookings_model import Booking

class CreateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['rooms', 'booking_name', 'phone_num','no_of_guest', 'check_in', 'check_out','description']