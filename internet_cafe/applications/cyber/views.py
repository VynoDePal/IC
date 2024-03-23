from django.shortcuts import render
from rest_framework import viewsets

from .models import ComputerSession
from .serializers import ComputerSessionSerializer


# Create your views here.
class ComputerSessionView(viewsets.ModelViewSet):
    serializer_class = ComputerSessionSerializer
    queryset = ComputerSession.objects.all()
