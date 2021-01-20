from django.db import models
from model_utils.models import TimeStampedModel


class Client(TimeStampedModel):
    kakaotalk_id = models.CharField(max_length=128, unique=True)
