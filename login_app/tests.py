from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient


class AuthFlowTests(TestCase):
    def setUp(self):
        # Usuario de prueba
        self.username = "tester"
        self.password = "StrongPass#123"
        get_user_model().objects.create_user(
            username=self.username, password=self.password
        )
        self.client = APIClient()

    def test_health_ok(self):
        """ /api/health/ debe responder 200 con {"status": "ok"} """
        url = reverse("api_health")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), {"status": "ok"})

    def test_login_returns_token(self):
        """ /api/login/ debe devolver token con credenciales válidas """
        url = reverse("api_login")
        payload = {"username": self.username, "password": self.password}
        res = self.client.post(url, payload, format="json")
        self.assertEqual(res.status_code, 200)
        self.assertIn("token", res.json())


# Create your tests here.
