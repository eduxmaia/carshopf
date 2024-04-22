from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20, unique=True, default='unknown')
    cpf = models.CharField(max_length=15)
    profile = models.CharField(max_length=100,choices=[('admin', 'Admin'), ('user', 'User')])

    def __str__(self):
        return self.username
