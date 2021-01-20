"""Land LIVE+ API URL Configuration
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path

V = settings.API_VERSION

urlpatterns = [
    path('admin/', admin.site.urls),
]
