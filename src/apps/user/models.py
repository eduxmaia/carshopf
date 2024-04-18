from django.db import models


# Create your models here.

class User(models.Model):
    cpf = models.CharField(max_length=15)
    profile = models.CharField(max_length=100,choices=[('admin', 'Admin'), ('user', 'User')])
