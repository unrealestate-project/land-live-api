from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from api.models.real_estate.models import RealEstate
from .serializers import RealEstateToursSerializer


class RealEstateAvailTourViewSet(viewsets.ModelViewSet):
    queryset = RealEstate.objects.all()
    lookup_url_kwarg = 'real_estate_id'
    serializer_class = RealEstateToursSerializer

    def list(self, request, *args, **kwargs):
        real_estate = self.get_object()
        serializer = self.get_serializer(real_estate)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class TourBookingViewSet(viewsets.ModelViewSet):
#     queryset = Tour.objects.all()
#     lookup_url_kwarg = 'tour_id'
#
#     def create(self, request, *args, **kwargs):
#         return
