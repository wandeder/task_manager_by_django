from django.contrib.auth.forms import UserCreationForm
from task_manager.models import User, Status
from django.forms import ModelForm


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class StatusCreationForm(ModelForm):
    class Meta:
        model = Status
        fields = ['name']
