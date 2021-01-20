"""Land LIVE+ API URL Configuration
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from api.services.booking import urls as booking_urls

V = settings.API_VERSION

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'api/{V}/booking/', include(booking_urls)),
]
