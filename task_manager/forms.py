from django.contrib.auth.forms import UserCreationForm
from task_manager.models import User, Status, Task
from django.forms import ModelForm, Textarea, ModelChoiceField


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class StatusCreationForm(ModelForm):
    class Meta:
        model = Status
        fields = ['name']


class TaskCreationForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'form-group'

    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor')
