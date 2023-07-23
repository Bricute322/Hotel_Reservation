from client_hotel_reservation.models.bookings_model import Booking
from client_hotel_reservation.models.availability_model import Availability

class BookingChecker:
    def validate_existing_booking_date(self,room,check_in,check_out):

        overlapping_availability = Availability.objects.filter(
                booking__rooms=room,
                check_out__gte=check_in,
                check_in__lte=check_out,
                is_archive = False,
            )

        if overlapping_availability.exists():
            return {'error': 'Room is not available for the specified period.'}
        
        return
        
    def validate_room_uid():
        pass
    def validate_field(self,request):
        errors ={}

        if 'phone_num' in request.data and request.data['phone_num'] == '':
            errors['phone_number'] =  'Phone number should not be empty'

        if len(request.data['phone_num']) != 11:
            errors['phone_number'] = 'Please Enter a valid phone number'

        if request.data['phone_num'][:2] != '09':
            errors['phone_number'] = 'Please Enter Philippine-based mobile number'

        return errors
    

    
