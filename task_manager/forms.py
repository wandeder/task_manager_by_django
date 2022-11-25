from django.contrib.auth.forms import UserCreationForm
from task_manager.models import user, status, task, label
from django.forms import ModelForm, Textarea, ModelChoiceField


class UserCreationForm(UserCreationForm):
    title = 'user'

    class Meta(UserCreationForm.Meta):
        model = user


class StatusCreationForm(ModelForm):
    title = 'status'

    class Meta:
        model = status
        fields = ['name']


class TaskCreationForm(ModelForm):
    title = 'task'
    error_css_class = 'error'
    # required_css_class = 'form-group'

    class Meta:
        model = task
        fields = ('name', 'description', 'status', 'executor', 'labels',)


class LabelCreationForm(ModelForm):
    title = 'label'

    class Meta:
        model = label
        fields = ['name']
