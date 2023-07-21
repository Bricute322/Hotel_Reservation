from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.room_details_serializer import ListRoomSerializer
from client_hotel_reservation.models.rooms_model import Room

class RoomDetailsAPI(APIView):
    def get(self, request, *args, **kwargs):
        ### Add Field Validator Here ####

        #################################
        
        room_uid = request.query_params['uid']
        room = Room.objects.get(uid=room_uid)
        serializer = ListRoomSerializer(room)
        
        return Response({'message': 'Success', 'data': serializer.data}, status=status.HTTP_200_OK)