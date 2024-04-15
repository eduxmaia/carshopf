from django.db import models


# Create your models here.

class Vacancy(models.Model):
    class Vacancy(models.Model):
        VACANCY_TYPE_CHOICES = [
            ('simple', 'Simple'),
            ('double', 'Double'),
            ]
        vacancy_type = models.CharField(max_length=100, choices=VACANCY_TYPE_CHOICES)
    value = models.DecimalField(max_digits=15, decimal_places=2)
