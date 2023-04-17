from django.db import models
from django.contrib.auth.models import User

from datetime import timezone

# Create your models here.
class LeadModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="leads", null=True)

    def __str__(self):
        return self.name