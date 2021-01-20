from django.db import models
from model_utils.models import TimeStampedModel

from api.models.broker.models import Broker


class RealEstate(TimeStampedModel):
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    zigbang_link = models.URLField(null=True, blank=True)
    dabang_link = models.URLField(null=True, blank=True)
    naver_estate_link = models.URLField(null=True, blank=True)
    peterpan_link = models.URLField(null=True, blank=True)
