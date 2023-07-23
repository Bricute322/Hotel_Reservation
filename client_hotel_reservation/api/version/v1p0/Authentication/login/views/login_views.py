from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth import authenticate
from ..serializers.login_serializer import UserLoginSerializer
from client_hotel_reservation.validators.custom_authenticate import EmailBackend

class UserLoginView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid:

            email = request.data['email']
            password = request.data['password']
            
            user = EmailBackend.authenticate(EmailBackend,request,email=email, password=password)

            if user is None:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
        
            return Response({'messsage': 'Success','access_token': access_token}, status=status.HTTP_200_OK)
        
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)