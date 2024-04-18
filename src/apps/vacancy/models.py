from django.db import models


# Create your models here.

class Vacancy(models.Model):
    vacancy_choices = (
        ('simple', 'Simple'),
        ('double', 'Double')
    )
    vacancy_type = models.CharField(choices=vacancy_choices, max_length=15)
    price = models.DecimalField(max_digits=10, decimal_places=2)
