from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from ..serializers.register_serializer import UserRegistrationSerializer
from django.contrib.auth.hashers import make_password
from client_hotel_reservation.validators.user_helper import UserHelper
class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        errors = UserHelper.validate_data(self,request)
        
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            user = User.objects.create(
                username = request.data['username'],
                email = request.data['email'],
                password = make_password(request.data['password'])
            )
            return Response({'message': 'User registered successfully!', 'user_id': user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)