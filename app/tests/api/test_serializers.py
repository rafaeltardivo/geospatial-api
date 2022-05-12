from django.test import TestCase

from api.serializers import ATMSerializer
from django.contrib.gis.geos import GEOSGeometry

from .factories import ATMFactory


class TestATMSerializer(TestCase):
    def setUp(self):
        self.instance = ATMFactory()
        self.serializer = ATMSerializer(instance=self.instance)

    def test_content(self):
        self.assertEqual(self.instance.address, self.serializer.data["address"])
        self.assertEqual(self.instance.provider, self.serializer.data["provider"])
        self.assertEqual(
            self.instance.geometry, GEOSGeometry(str(self.serializer.data["geometry"]))
        )
