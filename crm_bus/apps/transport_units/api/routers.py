from rest_framework.routers import DefaultRouter
from django.urls import path, include

from apps.transport_units.api.views import general_views
from apps.transport_units.api.views import transport_unit_views

router = DefaultRouter()

router.register(r'transports_units', transport_unit_views.TransportUnitViewSet, 'transports_units')

urlpatterns = [
    path('fuel_type/', general_views.FuelTypeAPIView.as_view(), name='fuel_type'),
    path('transport_type/', general_views.TransportTypeAPIView.as_view(), name='transport_type'),
    path('', include(router.urls))
]
