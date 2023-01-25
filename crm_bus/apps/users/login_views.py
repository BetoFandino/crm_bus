from django.contrib.auth import authenticate, login, logout

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
            login(request, user)

            return Response({'message': 'exitooo'})
        else:
            return Response({'error': 'username or password incorrect'}, status=status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        if user:
            RefreshToken.for_user(user)
            return Response({'message': 'Logout success.'}, status=status.HTTP_200_OK)
        return Response({'error': 'user not found.'}, status=status.HTTP_400_BAD_REQUEST)
