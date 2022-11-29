from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from task_manager.models import user, status, task, label
from django.forms import ModelForm, Textarea, ModelChoiceField, CharField, PasswordInput, ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from collections import OrderedDict


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

    password1 = CharField(label=_("New password"), widget=PasswordInput)
    password2 = CharField(label=_("New password confirmation"), widget=PasswordInput)

    class Meta:
        model = user

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['password1'])
        if commit:
            self.user.save()
        return self.user


PasswordUpdateForm.base_fields = OrderedDict(
    (k, PasswordUpdateForm.base_fields[k])
    for k in ['password1', 'password2']
)
