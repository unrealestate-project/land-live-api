from django.db import models
from model_utils.models import TimeStampedModel


class Client(TimeStampedModel):
    kakaotalk_id = models.CharField(max_length=255, unique=True)

    USERNAME_FIELD = 'kakaotalk_id'
    REQUIRED_FIELDS = ()
