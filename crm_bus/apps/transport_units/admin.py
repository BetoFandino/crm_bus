from django.contrib import admin

from apps.transport_units import models

admin.site.register(models.FuelType)
admin.site.register(models.TransportType)
admin.site.register(models.TransportUnit)
