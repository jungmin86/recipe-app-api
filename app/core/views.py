"""
Core views for app.
"""
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import HealthCheckSerializer


class HealthCheckAPIView(GenericAPIView):
    serializer_class = HealthCheckSerializer

    def get(self, request):
        data = {"healthy": True}
        return Response(data)
