from django.db import models
from model_utils.models import TimeStampedModel


class Broker(TimeStampedModel):
    kakaotalk_id = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=64)
    office_name = models.CharField(max_length=128, null=True, blank=True)
    office_address = models.CharField(max_length=256, null=True, blank=True)
