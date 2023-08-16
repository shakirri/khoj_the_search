from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=20, primary_key=True, serialize=False)
    authentication = models.CharField(default=None, blank=True, null=True, max_length=50)
    
class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_values = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=datetime.now()) 