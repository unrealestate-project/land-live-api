from django.urls import path

from .views import (
    RealEstateAvailTourViewSet,
)

urlpatterns = [
    path('real_estates/<real_estate_id>/tours', RealEstateAvailTourViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
]
