from django.urls import path
from apps.users.api.api import UserViewSet

urlpatterns = [
    path('users/', UserViewSet.as_view, name='user_api')
]
