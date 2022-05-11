from rest_framework.generics import ListCreateAPIView

from .models import ATM
from .serializers import ATMSerializer


class ATMView(ListCreateAPIView):
    """ATM List/Create view."""

    queryset = ATM.objects.all()
    serializer_class = ATMSerializer
