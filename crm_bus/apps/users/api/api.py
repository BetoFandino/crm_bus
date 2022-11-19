from rest_framework.response import Response
from rest_framework import status

from apps.users.api.serializers import UserSerializer, UpdateUserSerializer, ListUserSerializer
from apps.base.api.generic_api import BaseGenericViewSet


class UserViewSet(BaseGenericViewSet):
    serializer_class = UserSerializer
    list_serializer_class = ListUserSerializer
    update_serializer_class = UpdateUserSerializer
    model_object = 'User'
    queryset = None

    def get_queryset(self):
        if self.queryset is None:
            model = self.get_serializer().Meta.model
            self.queryset = model.objects.filter(is_active=True).values('id', 'username', 'email', 'name')
        return self.queryset

    def destroy(self, request, pk=None):
        model = self.get_serializer().Meta.model
        user_destroy = model.objects.filter(id=pk).update(is_active=False)
        if user_destroy == 1:
            return Response({
                'message': 'user deleted'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': "user don't found"
        }, status=status.HTTP_400_BAD_REQUEST)
