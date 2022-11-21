from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from task_manager.forms import UserCreationForm, StatusCreationForm
from task_manager.models import Status

User = get_user_model()


class HomeView(TemplateView):
    model = User
    template_name = 'home.html'


class UsersList(ListView):
    model = User
    context_object_name = 'users_list'
    template_name = 'users_list.html'


class StatusesList(ListView):
    model = Status
    context_object_name = 'statuses_list'
    template_name = 'statuses_list.html'


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'user_create_form.html'
    success_url = reverse_lazy('login')
    success_message = '\"%(username)s\" your account has been successfully created.'


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'user_update_form.html'
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy('users_list')
    success_message = '\"%(username)s\" your account has been successfully updated.'


class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'user_delete_form.html'
    success_url = reverse_lazy('users_list')
    success_message = 'Your account has been successfully deleted.'


class StatusCreateView(SuccessMessageMixin, CreateView):
    form_class = StatusCreationForm
    template_name = 'status_create_form.html'
    success_url = reverse_lazy('statuses_list')
    success_message = 'Status \"%(name)s\" was created successfully.'


class StatusUpdateView(SuccessMessageMixin, UpdateView):
    model = Status
    template_name = 'status_update_form.html'
    fields = ['name', ]
    success_url = reverse_lazy('statuses_list')
    success_message = 'Status \"%(name)s\" was updated successfully.'


class StatusDeleteView(SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'status_delete_form.html'
    success_url = reverse_lazy('statuses_list')
    success_message = 'Status was deleted successfully.'
