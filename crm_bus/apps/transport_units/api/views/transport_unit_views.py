from apps.transport_units.api.serializers import transport_unit_serializer

from apps.base.api.generic_api import BaseGenericViewSet


class TransportUnitViewSet(BaseGenericViewSet):
    serializer_class = transport_unit_serializer.TransportUnitSerializer
    list_serializer_class = transport_unit_serializer.TransportUnitListSerializer
    update_serializer_class = transport_unit_serializer.TransportUnitSerializer
    model_object = 'Transport unit'
    