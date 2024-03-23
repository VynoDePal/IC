from rest_framework import serializers
from .models import ComputerSession


class ComputerSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerSession
        fields = '__all__'
