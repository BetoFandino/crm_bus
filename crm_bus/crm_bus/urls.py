from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users import login_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_views.Login.as_view(), name='login'),
    path('logout/', login_views.Logout.as_view(), name='logout'),
    path('users/', include('apps.users.api.routers')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('employees/', include('apps.employees.api.routers')),
    path('transports_units/', include('apps.transport_units.api.routers'))
]
