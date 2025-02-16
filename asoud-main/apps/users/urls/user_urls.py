from django.urls import path

from apps.users.views.user_views import PinCreateAPIView, PinVerifyAPIView

app_name = 'users_user'

urlpatterns = [
    path('pin/create/', PinCreateAPIView.as_view(), name='pin-create'),
    path('pin/verify/', PinVerifyAPIView.as_view(), name='pin-verify'),
]
