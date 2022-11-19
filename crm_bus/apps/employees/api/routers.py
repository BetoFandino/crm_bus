from rest_framework.routers import DefaultRouter
from django.urls import path, include

from apps.employees.api.views import general_views
from apps.employees.api.views import employee_view

router = DefaultRouter()

router.register(r'employees', employee_view.EmployeeViewSet, 'employees')
# router.register(r'roles', general_views.RoleListAPIView.as_view(), 'roles')

urlpatterns = [
    path('roles/', general_views.RoleListAPIView.as_view(), name='roles'),
    #path('employees/', employee_view.EmployeeViewSet.as_view(), name='employees'),
    path('', include(router.urls))
]
