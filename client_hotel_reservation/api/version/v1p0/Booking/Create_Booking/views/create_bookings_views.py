from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.create_bookings_serializers import CreateBookingSerializer
from client_hotel_reservation.models.bookings_model import Booking
from client_hotel_reservation.models.rooms_model import Room

class CreateBookingAPI(APIView):
    def post(self,request, *args, **kwargs):
        ### Add Field Validator Here ####

        #################################

        serializer = CreateBookingSerializer(data=request.data)
        
        if serializer.is_valid():
            room_id = request.query_params['rooms']
            room = Room.objects.get(uid=room_id)

            Booking.objects.create(
                rooms = room,
                booking_name = request.data['booking_name'],
                phone_num = request.data['phone_num'],
                no_of_guest = request.data['no_of_guest'],
                check_in = request.data['check_in'],
                check_out = request.data['check_out'],
                description = request.data['description'],
            )
            room.availability = False
            room.save()
            return Response({'message': 'Booking Successfuly Created', 'data' : serializer.data}, status=status.HTTP_201_CREATED)
        else:
            pass
        return Response({'message': 'error', 'error' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)