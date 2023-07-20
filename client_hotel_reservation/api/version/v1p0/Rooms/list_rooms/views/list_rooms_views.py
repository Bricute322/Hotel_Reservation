from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.rooms_serializer import ListRoomSerializer
from client_hotel_reservation.models.rooms_model import Room

class ListRoomsAPI(APIView):
    def get(self, request, *args, **kwargs):
        ### Add Field Validator Here ####

        #################################
        
        hotel_uid = request.query_params.get('uid')
        rooms = Room.objects.filter(hotel=hotel_uid)
        serializer = ListRoomSerializer(rooms, many=True)
        
        return Response({'message': 'Success', 'data': serializer.data}, status=status.HTTP_200_OK)
