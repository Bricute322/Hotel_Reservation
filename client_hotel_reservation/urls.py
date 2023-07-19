from django.urls import path
from .api.version.v1p0.Hotel.list_hotel.views.list_hotel_views import ListHotel

urlpatterns = [
    path('hotels/', ListHotel.as_view(), name = 'client_list_hotel'),
]