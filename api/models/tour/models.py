from django.db import models
from model_utils.models import TimeStampedModel

from api.models.real_estate.models import RealEstate


class Tour(TimeStampedModel):
    real_estate = models.ForeignKey(RealEstate, on_delete=models.DO_NOTHING)
    streaming_date = models.DateTimeField(null=False, blank=False)
    streaming_duration_min = models.IntegerField(null=False, blank=False)
    streaming_link = models.URLField()
    min_book_client = models.IntegerField(null=False, blank=False)
