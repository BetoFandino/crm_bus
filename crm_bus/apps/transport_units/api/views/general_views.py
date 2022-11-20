from rest_framework import generics

from apps.transport_units.api.serializers import general_serializer
from apps.base.api.list_api import GenericListAPIView


class FuelTypeAPIView(generics.ListAPIView):
    serializer_class = general_serializer.FuelTypeListSerializer

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.all()


class TransportTypeAPIView(GenericListAPIView):
    serializer_class = general_serializer.TransportTypeSerializer
