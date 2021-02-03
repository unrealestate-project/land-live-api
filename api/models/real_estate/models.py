import uuid

from django.db import models
from model_utils.models import TimeStampedModel

from api.models.broker.models import Broker


def hex_uuid():
    return uuid.uuid4().hex[:10]


class RealEstate(TimeStampedModel):
    id = models.CharField(default=hex_uuid, primary_key=True, max_length=100)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    zigbang_link = models.URLField(null=True, blank=True)
    dabang_link = models.URLField(null=True, blank=True)
    naver_estate_link = models.URLField(null=True, blank=True)
    peterpan_link = models.URLField(null=True, blank=True)
