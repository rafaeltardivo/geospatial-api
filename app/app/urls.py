from django.urls import path, re_path
from api.views import ATMView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="ATM API", default_version="v1", description="Geospatial ATM API"
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("atm", ATMView.as_view(), name="atm"),
    re_path(
        r"^docs/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
