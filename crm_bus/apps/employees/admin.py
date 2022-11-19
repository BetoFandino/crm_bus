from django.contrib import admin
from apps.employees.models import Role, Employee


admin.site.register(Role)
admin.site.register(Employee)
