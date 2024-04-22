import uuid

from django.db import models

from apps.user.models import User
from apps.vacancy.models import Vacancy


class Parking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(max_length=10, unique=True, default=uuid.uuid4, editable=False)
    plate = models.CharField(max_length=10)
    brand = models.CharField(max_length=15)
    car_model = models.CharField(max_length=20)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car_model
