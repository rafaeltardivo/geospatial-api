from factory.django import DjangoModelFactory

from django.contrib.gis.geos import GEOSGeometry

from api.models import ATM


class ATMFactory(DjangoModelFactory):
    """ATM model factory."""

    class Meta:
        model = ATM

    address = "test address"
    provider = "test provider"
    geometry = GEOSGeometry(
        '{ "type": "Point", "coordinates": [49.2849777, -123.1189405]}'
    )
