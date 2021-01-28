from django.db import models
from model_utils.models import TimeStampedModel

from api.models.real_estate.models import RealEstate


class Tour(TimeStampedModel):
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    streaming_date = models.DateTimeField(null=True, blank=True)
    streaming_duration_min = models.IntegerField(null=True, blank=True)
    streaming_link = models.URLField(null=True, blank=True)
    min_book_client = models.IntegerField(null=True, blank=True)
