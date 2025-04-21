from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from authentication.views import (
    RegisterView,
    LoginView,
    ChangePasswordView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]