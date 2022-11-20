import os

from django.http import FileResponse

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from apps.transport_units.api.serializers import transport_unit_serializer
from apps.base.api.generic_api import BaseGenericViewSet
from general_operations.export_excel import operations

import response_codes


class TransportUnitViewSet(BaseGenericViewSet):
    serializer_class = transport_unit_serializer.TransportUnitSerializer
    list_serializer_class = transport_unit_serializer.TransportUnitListSerializer
    update_serializer_class = transport_unit_serializer.TransportUnitSerializer
    model_object = 'Transport unit'

    @action(methods=['post'], url_path='export', detail=False)
    def export_excel(self, request):
        response = self.list(request)
        if response.data:
            excel = operations.MakeExcelData(data=response.data, title='Transport Unit', special_value='name')
            excel.delete_excel(0)
            return_code, filename = excel.excel_generator()

            if return_code == response_codes.SUCCESS:
                file = open(filename, 'rb')
                response = FileResponse(file)
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(filename)
            else:
                response = Response({
                    'Error': 'The file not make'},
                    status=status.HTTP_409_CONFLICT
                )
        else:
            response = Response({
                'message': 'not found transport units'},
                status=status.HTTP_200_OK
            )
        return response
