from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Status(models.Model):
    name = models.CharField(max_length=50)


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+')
    executor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+')
