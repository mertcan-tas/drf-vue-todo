from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('account.urls')),
    path('api/auth/', include('authentication.urls')),
    path('', include('testing.urls')),
    path('api/', include('api.urls')),
]


