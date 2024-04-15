from django.db import models

from apps.user.models import User
from apps.vacancy.models import Vacancy


class Parking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    plate = models.CharField(max_length=10)
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
