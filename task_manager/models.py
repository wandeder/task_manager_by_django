from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class user(AbstractUser):
    pass


class status(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class label(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=700)
    status = models.ForeignKey(status, on_delete=models.PROTECT)
    creator = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='creator')
    executor = models.ForeignKey(user, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField(label, through="labels_of_task")

    def __str__(self):
        return self.name


class labels_of_task(models.Model):
    task = models.ForeignKey(task, on_delete=models.CASCADE)
    label = models.ForeignKey(label, on_delete=models.PROTECT)
