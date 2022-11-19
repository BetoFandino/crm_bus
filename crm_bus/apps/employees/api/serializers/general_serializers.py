from rest_framework import serializers

from apps.employees import models


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Role
        exclude = ('id', 'state', 'created_date', 'modified_date', 'deleted_date')
