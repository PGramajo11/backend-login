from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

class HealthView(APIView):
    permission_classes = [AllowAny]  # público, sin token
    def get(self, request):
        return Response({"status": "ok"})

class HelloView(APIView):
    permission_classes = [IsAuthenticated]  # requiere token
    def get(self, request):
        return Response({"message": f"Hola, {request.user.username}! Autenticación OK ✅"})

# Create your views here.
