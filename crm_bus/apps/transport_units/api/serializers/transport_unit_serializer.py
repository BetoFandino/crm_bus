from rest_framework import serializers

from apps.transport_units.models import TransportUnit


class TransportUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransportUnit
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class TransportUnitListSerializer(serializers.ModelSerializer):
    transport_type = serializers.StringRelatedField()

    class Meta:
        model = TransportUnit
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
