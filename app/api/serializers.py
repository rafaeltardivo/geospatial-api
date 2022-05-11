from rest_framework import serializers

from .models import ATM


class ATMSerializer(serializers.ModelSerializer):
    """ATM serializer."""

    class Meta:
        model = ATM
        fields = ("id", "geometry", "address", "provider")
        read_only_fields = ("id",)
