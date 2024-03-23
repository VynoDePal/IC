from django.contrib.auth import get_user_model
from django.db import models

from applications.session.models import Session


# Create your models here.
class Pago(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    rising = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.rising}"

