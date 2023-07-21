from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.list_booking_serializer import ListBookingSerializer
from client_hotel_reservation.models.bookings_model import Booking

class ListBookingAPI(APIView):
    def get(self,request):
        bookings = Booking.objects.filter(is_archive = False)
        serializer = ListBookingSerializer(bookings,many=True)
        
        return Response({'message': 'Success', 'data': serializer.data}, status=status.HTTP_200_OK)