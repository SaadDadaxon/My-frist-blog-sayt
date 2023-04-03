from rest_framework.response import Response
from rest_framework import generics, status, permissions

from ..models import About
from .serializers import AboutSerializers


class AboutListCreateAPI(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializers
