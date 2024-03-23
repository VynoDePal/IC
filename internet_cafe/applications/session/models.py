from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
User = get_user_model()


class Tarifa(models.Model):
    nombre = models.CharField(max_length=255)
    cost_per_hour = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.nombre


class ComputerSession(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    in_use = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


class Session(models.Model):
    computer = models.ForeignKey(ComputerSession, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tarifa = models.ForeignKey(Tarifa, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} - {self.computer.nombre}"
