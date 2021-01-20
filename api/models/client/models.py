from django.db import models
from model_utils.models import TimeStampedModel

from api.models.tour.models import Tour


class Client(TimeStampedModel):
    kakaotalk_id = models.CharField(max_length=128, unique=True)
    booked_tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
