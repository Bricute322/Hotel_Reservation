from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.create_bookings_serializers import CreateBookingSerializer
from client_hotel_reservation.models.bookings_model import Booking
from client_hotel_reservation.models.availability_model import Availability
from client_hotel_reservation.models.rooms_model import Room

class CreateBookingAPI(APIView):
    def post(self,request, *args, **kwargs):
        ### Add Field Validator Here ####

        #################################

        serializer = CreateBookingSerializer(data=request.data)
        
        if serializer.is_valid():
            room_id = request.query_params['rooms']
            room = Room.objects.get(uid=room_id)

            check_in = request.data['check_in']
            check_out = request.data['check_out']
            
            booking = Booking.objects.create(
                rooms = room,
                booking_name = request.data['booking_name'],
                phone_num = request.data['phone_num'],
                no_of_guest = request.data['no_of_guest'],
                description = request.data['description'],
            )

            overlapping_availability = Availability.objects.filter(
                booking__rooms=room,
                check_out__gte=check_in,
                check_in__lte=check_out,
                is_archive = False,
            )

            if overlapping_availability.exists():
                booking.delete()
                return Response({'message': 'Room is not available for the specified period.'}, status=status.HTTP_400_BAD_REQUEST)
           
            Availability.objects.create(booking=booking, check_in=check_in, check_out=check_out)
            serialized_booking = serializer.data
            serialized_booking['rooms'] = {
                'uid': room.uid,
                'room_number': room.room_no,
                'room_type': room.room_type,
            }
            return Response({'message': 'Booking Successfuly Created', 'data' : serialized_booking}, status=status.HTTP_201_CREATED)
        
        return Response({'message': 'error', 'error' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)