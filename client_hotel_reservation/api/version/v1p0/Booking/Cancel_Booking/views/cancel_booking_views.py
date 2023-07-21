from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from client_hotel_reservation.models.bookings_model import Booking
from client_hotel_reservation.models.availability_model import Availability
from client_hotel_reservation.models.rooms_model import Room

class UpdateBookingAPI(APIView):
    def put(self,request, *args, **kwargs):
        ### Add Field Validator Here ####

        #################################
        booking_id = request.query_params['booking_id']
        try:
            booking = Booking.objects.get(uid=booking_id)
        except Booking.DoesNotExist:
            return Response({'message': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)

        booking.is_archive = True
        booking.save()

        availability = Availability.objects.filter(booking=booking)
        availability.update(is_archive=True)
        
        return Response({'message': 'Booking Successfuly Cancelled'}, status=status.HTTP_201_CREATED)