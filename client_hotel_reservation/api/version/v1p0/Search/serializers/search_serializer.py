from rest_framework import serializers
from client_hotel_reservation.models.rooms_model import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['uid', 'hotel', 'room_no', 'room_type', 'max_guest']