from django.urls import path
from .api.version.v1p0.Hotel.list_hotel.views.list_hotel_views import ListHotelAPI
from .api.version.v1p0.Booking.Create_Booking.views.create_bookings_views import CreateBookingAPI
from .api.version.v1p0.Rooms.list_rooms.views.list_rooms_views import ListRoomsAPI

urlpatterns = [
    
    ############ Hotels #############

    path('hotels/list/', ListHotelAPI.as_view(), name = 'client_list_hotel'),

    ############ bookings #############

    path('booking/add/', CreateBookingAPI.as_view(), name = 'client_add_booking'),

    ############ Rooms ###############

    path('rooms/list/', ListRoomsAPI.as_view(), name = 'client_list_rooms'),

]