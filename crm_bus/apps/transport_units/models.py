from django.db import models

from apps.base.models import BaseModel


class FuelType(models.Model):
    fuel_type = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Fuel type'
        verbose_name_plural = 'Fuels types'

    def __str__(self):
        return self.fuel_type


class TransportType(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    capacity = models.IntegerField()
    fuel_type = models.ManyToManyField(FuelType)
    description = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Transport type'
        verbose_name_plural = 'Transports Types'

    def __str__(self):
        return self.name


class TransportUnit(BaseModel):
    unit_id = models.IntegerField(unique=True)
    description = models.CharField(max_length=100, null=True, blank=False)
    transport_type = models.ForeignKey(TransportType, on_delete=models.CASCADE)
    plate = models.CharField(max_length=50, unique=True)
    last_maintenance_date = models.DateField(null=True)

    class Meta:
        verbose_name = 'Transport Unit'
        verbose_name_plural = 'Transports Units'

    def __str__(self):
        return self.unit_id
