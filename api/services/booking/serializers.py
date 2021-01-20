from rest_framework import serializers

from api.models.real_estate.models import RealEstate
from api.models.tour.models import Tour


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['id', 'streaming_date', 'streaming_duration_min']


class RealEstateToursSerializer(serializers.ModelSerializer):
    tours = serializers.ListField(read_only=True)

    def to_representation(self, instance):
        tours = Tour.objects.filter(real_estate=instance)
        instance.tours = TourSerializer(tours, many=True).data
        return super().to_representation(instance)

    class Meta:
        model = RealEstate
        fields = ['tours']
