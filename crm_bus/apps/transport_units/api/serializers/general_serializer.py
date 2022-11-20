from rest_framework import serializers

from apps.transport_units import models


class FuelTypeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FuelType
        fields = '__all__'


class FuelTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FuelType
        fields = ('fuel_type',)


class TransportTypeSerializer(serializers.ModelSerializer):
    fuel_type = FuelTypeSerializer(models.FuelType, many=True)

    class Meta:
        model = models.TransportType
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
