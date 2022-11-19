from rest_framework import serializers

from apps.employees import models


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Employee
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class EmployeeListSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()

    class Meta:
        model = models.Employee
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class UpdateEmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Employee
        fields = ('name', 'last_name', 'identification', 'role', 'description')
