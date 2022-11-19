from apps.employees.api.serializers import employee_serializers

from apps.base.api.generic_api import BaseGenericViewSet


class EmployeeViewSet(BaseGenericViewSet):
    serializer_class = employee_serializers.EmployeeSerializer
    list_serializer_class = employee_serializers.EmployeeListSerializer
    update_serializer_class = employee_serializers.UpdateEmployeeSerializer
    model_object = 'Employee'
