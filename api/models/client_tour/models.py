from django.db import models
from model_utils.models import TimeStampedModel

from api.models.client.models import Client
from api.models.tour.models import Tour


class ClientTour(TimeStampedModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
