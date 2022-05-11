from rest_framework import generics

from .models import ATM
from .serializers import ATMSerializer


class ATMView(generics.ListCreateAPIView):
    queryset = ATM.objects.all()
    serializer_class = ATMSerializer
