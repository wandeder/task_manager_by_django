from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class user(AbstractUser):

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class status(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class label(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class task(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.TextField(
            max_length=700,
            verbose_name=_('Description')
    )
    status = models.ForeignKey(
            status, on_delete=models.PROTECT,
            verbose_name=_('Status'),
    )
    creator = models.ForeignKey(
            get_user_model(),
            on_delete=models.PROTECT,
            related_name='creator',
    )
    executor = models.ForeignKey(
            user, on_delete=models.PROTECT,
            null=True, verbose_name=_('Executor'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField(
            label,
            through="labels_of_task",
            verbose_name=_('Labels'),
    )

    def __str__(self):
        return self.name


class labels_of_task(models.Model):
    task = models.ForeignKey(task, on_delete=models.CASCADE)
    label = models.ForeignKey(label, on_delete=models.PROTECT)
