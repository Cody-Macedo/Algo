from datetime import datetime, date

from django.db import models
from django import forms


# Create your models here.


class Task(models.Model):
    content = models.CharField(max_length=255, default='NaN')
    is_done = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

