from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import HelloView, HealthView   # ← importante

urlpatterns = [
    path("login/", obtain_auth_token, name="api_login"),
    path("hello/", HelloView.as_view(), name="api_hello"),
    path("health/", HealthView.as_view(), name="api_health"),
]
