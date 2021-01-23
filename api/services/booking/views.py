from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from api.models.client.models import Client
from api.models.real_estate.models import RealEstate
from api.models.tour.models import Tour
from .serializers import RealEstateToursSerializer, BookTourSerializer


class RealEstateAvailTourViewSet(viewsets.ModelViewSet):
    queryset = RealEstate.objects.all()
    lookup_url_kwarg = 'real_estate_id'

    def get_serializer_class(self):
        if self.action == 'create':
            return BookTourSerializer
        return RealEstateToursSerializer

    def list(self, request, *args, **kwargs):
        real_estate = self.get_object()
        serializer = self.get_serializer(real_estate)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        kakaotalk_id = request.data.get('kakaotalk_id')
        client, _ = Client.objects.get_or_create(kakaotalk_id=kakaotalk_id)
        real_estate = self.get_object()
        tour = Tour.objects.get(real_estate=real_estate)
        serializer = self.get_serializer(data={'client': client.id,
                                               'tour': tour.id})
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except ValidationError:
            return Response({'data': 'Already booked this tour!'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return Response({'data': 'Successfully booked!'},
                        status=status.HTTP_200_OK)
