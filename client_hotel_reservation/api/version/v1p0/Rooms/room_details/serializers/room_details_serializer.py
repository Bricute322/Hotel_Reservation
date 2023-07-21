from rest_framework import serializers
from client_hotel_reservation.models.rooms_model import Room

class ListRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['uid', 'hotel', 'room_no', 'room_type','room_image', 'max_guest','description']