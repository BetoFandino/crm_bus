from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.api.routers')),
    path('employees/', include('apps.employees.api.routers')),
    path('transports_units/', include('apps.transport_units.api.routers'))
]
