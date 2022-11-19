from apps.employees.api.serializers import general_serializers
from apps.base.api.list_api import GenericListAPIView


class RoleListAPIView(GenericListAPIView):
    serializer_class = general_serializers.RoleSerializer
