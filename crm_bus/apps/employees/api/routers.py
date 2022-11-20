from rest_framework.routers import DefaultRouter
from django.urls import path, include

from apps.employees.api.views import general_views
from apps.employees.api.views import employee_view

router = DefaultRouter()

router.register(r'employees', employee_view.EmployeeViewSet, 'employees')

urlpatterns = [
    path('roles/', general_views.RoleListAPIView.as_view(), name='roles'),
    path('', include(router.urls))
]
