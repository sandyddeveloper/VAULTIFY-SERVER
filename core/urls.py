from django.urls import path
from .views import UserInfoAPIView

urlpatterns = [
    path('api/user/', UserInfoAPIView.as_view(), name='user-info'),
]
