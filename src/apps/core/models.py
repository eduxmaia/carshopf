import uuid
import uuid as uuid_lib
from django.contrib.auth.models import User
from django.db import models

from apps.vacancy.models import Vacancy


class Parking(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(max_length=10)
    plate = models.CharField(max_length=10)
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=20)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
