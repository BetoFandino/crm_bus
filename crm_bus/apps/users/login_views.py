from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.api.serializers import (
    CustomTokenObtainPairSerializer, CustomUserSerializer
)


class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'login success'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'username or password incorrect'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'username or password incorrect'}, status=status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        if user:
            RefreshToken.for_user(user)
            return Response({'message': 'Logout success.'}, status=status.HTTP_200_OK)
        return Response({'error': 'user not found.'}, status=status.HTTP_400_BAD_REQUEST)
