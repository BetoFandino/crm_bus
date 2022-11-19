from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status


class BaseGenericViewSet(viewsets.GenericViewSet):
    serializer_class = None
    list_serializer_class = None
    update_serializer_class = None
    model_object = None
    queryset = None

    def get_object(self, pk):
        model = self.get_serializer().Meta.model
        return get_object_or_404(model, pk=pk)

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        if self.queryset is None:
            self.queryset = model.objects.filter(state=True)
        return self.queryset

    def list(self, request):
        object_generic = self.get_queryset()
        object_generic_serializer = self.list_serializer_class(object_generic, many=True)
        return Response(object_generic_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        object_generic_serializer = self.serializer_class(data=request.data)
        if object_generic_serializer.is_valid():
            object_generic_serializer.save()
            return Response({'message': '{} save success.'.format(self.model_object)}, status=status.HTTP_200_OK)
        return Response({'message': 'Have error/s in the form',
                         'errors': object_generic_serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        object_generic = self.get_object(pk)
        object_generic_serializer = self.serializer_class(object_generic)
        return Response(object_generic_serializer.data)

    def update(self, request, pk=None):
        object_generic = self.get_object(pk)
        object_generic_serializer = self.update_serializer_class(object_generic, data=request.data)
        if object_generic_serializer.is_valid():
            object_generic_serializer.save()
            return Response({
                'message': '{} updated success'.format(self.model_object)
            }, status=status.HTTP_200_OK)
        return Response({
            'message': ' Error in update {}'.format(self.model_object),
            'errors': object_generic_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        model = self.get_serializer().Meta.model
        user_destroy = model.objects.filter(id=pk).update(state=False)
        if user_destroy == 1:
            return Response({
                'message': '{} deleted'.format(self.model_object)
            }, status=status.HTTP_200_OK)
        return Response({
            'message': "{} don't found".format(self.model_object)
        }, status=status.HTTP_400_BAD_REQUEST)
