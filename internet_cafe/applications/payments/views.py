from django.shortcuts import render
from rest_framework import viewsets
from .models import Pago
from .serializers import PagoSerializer


# Create your views here.
class PagoView(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
