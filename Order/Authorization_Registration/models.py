from django.db import models

# Create your models here.
class Users(models.Model):
    login = models.CharField(max_length=255, default=0)
    password = models.IntegerField(default=0)
    email = models.CharField(max_length=255, default=0)
    phone = models.IntegerField(default=0)
