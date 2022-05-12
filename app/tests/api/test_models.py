from django.test import TestCase

from api.models import ATM

from .factories import ATMFactory


class TestATMModel(TestCase):
    def setUp(self):
        self.instance = ATMFactory()

    def test_create(self):
        self.assertIsInstance(self.instance, ATM)

    def test_str(self):
        self.assertEqual(
            str(self.instance), f"{self.instance.provider} - {self.instance.address}"
        )
