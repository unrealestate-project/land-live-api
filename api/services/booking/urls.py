from django.urls import path

from .views import (
    # TourBookingViewSet,
    RealEstateAvailTourViewSet,
)

urlpatterns = [
    path('real_estate/<real_estate_id>/tours', RealEstateAvailTourViewSet.as_view({
        'get': 'list',
    })),
    # path('real_estate/<real_estate_id>/tour/<tour_id>', TourBookingViewSet.as_view({
    #     'post': 'create',
    # })),
]
