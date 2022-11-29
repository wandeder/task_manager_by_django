from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from task_manager.models import user, status, task, label
from django.forms import ModelForm, Textarea, ModelChoiceField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import PasswordChangeForm


class UserCreationForm(UserCreationForm):
    button = _('Registrate')

    class Meta(UserCreationForm.Meta):
        model = user
        fields = ['first_name', 'last_name', 'username', ]


class StatusCreationForm(ModelForm):
    button = _('Create')

    class Meta:
        model = status
        fields = ['name']


class TaskCreationForm(ModelForm):
    button = _('Create')
    error_css_class = 'error'

    class Meta:
        model = task
        fields = ('name', 'description', 'status', 'executor', 'labels',)


class LabelCreationForm(ModelForm):
    button = _('Create')

    class Meta:
        model = label
        fields = ['name']


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = user
        fields = ['username', 'first_name', 'last_name', 'email', ]


class PasswordUpdateForm(PasswordChangeForm):

    class Meta:
        model = user
