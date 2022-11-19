from django.db import models

from apps.base.models import BaseModel


class Role(BaseModel):
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.name


class Employee(BaseModel):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    identification = models.IntegerField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
