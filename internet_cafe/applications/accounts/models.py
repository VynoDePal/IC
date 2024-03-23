from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    #class Meta:
        #app_label = 'accounts'

    ROLES = [
        ('ADMIN', 'admin'),
        ('USER', 'user'),
        ('COMPANY', 'company'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=7, choices=ROLES, default='USER')
