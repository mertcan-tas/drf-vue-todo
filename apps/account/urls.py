from django.urls import path

from account.views import (
    CurrentUserView,
)

urlpatterns = [    
    path('user/detail/', CurrentUserView.as_view(), name='user-detail'),
]