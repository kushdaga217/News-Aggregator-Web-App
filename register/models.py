from django.db import models

# Create your models here
class User(models.Model):
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)

    