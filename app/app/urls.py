from django.urls import path
from api.views import ATMView


urlpatterns = [
    path("atm", ATMView.as_view(), name="atm"),
]
