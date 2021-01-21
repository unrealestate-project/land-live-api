"""Land LIVE+ API URL Configuration
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView

from api.services.booking import urls as booking_urls

V = settings.API_VERSION

urlpatterns = [
    # ELB healthcheck handler
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path(f'api/{V}/booking/', include(booking_urls)),
]
