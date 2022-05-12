from django.urls import reverse
from rest_framework import test, status

from django.contrib.gis.geos import GEOSGeometry

from .factories import ATMFactory
from api.models import ATM


class TestATMView(test.APITransactionTestCase):
    def setUp(self):
        self.instance = ATMFactory()

    def test_list_atm(self):
        response = self.client.get(reverse("atm"))
        content = response.json()[0]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(content["address"], self.instance.address)
        self.assertEqual(content["provider"], self.instance.provider)
        self.assertEqual(self.instance.geometry, GEOSGeometry(str(content["geometry"])))

    def test_create_atm(self):
        before = ATM.objects.count()

        response = self.client.post(
            reverse("atm"),
            {
                "address": "test address",
                "provider": "test provider",
                "geometry": {
                    "type": "Point",
                    "coordinates": [49.2849777, -123.1189405],
                },
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        after = ATM.objects.count()
        self.assertEqual(after, before + 1)
