from django.db import models
from django.contrib.gis.db import models as gis_models


class ATM(models.Model):
    """ATM database object representation."""

    address = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    geometry = gis_models.PointField()
