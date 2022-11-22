from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from task_manager.forms import UserCreationForm, StatusCreationForm, TaskCreationForm
from task_manager.models import Status, Task
from django.http import HttpResponseRedirect
from django.db import models
from django.contrib import messages


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


class TasksList(ListView):
    model = Task
    context_object_name = 'tasks_list'
    template_name = 'tasks_list.html'


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

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except models.ProtectedError:
            messages.add_message(self.request, messages.ERROR,
                                 'Can not delete, because this user is used.')
            return HttpResponseRedirect(success_url)
        return HttpResponseRedirect(success_url)


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

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except models.ProtectedError:
            messages.add_message(self.request, messages.ERROR,
                                 'Can not delete, because this status is used.')
            return HttpResponseRedirect(success_url)
        return HttpResponseRedirect(success_url)


class TaskCreateView(SuccessMessageMixin, CreateView):
    form_class = TaskCreationForm
    template_name = 'task_create_form.html'
    success_url = reverse_lazy('tasks_list')
    success_message = 'Task \"%(name)s\" was created successfully.'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.creator = request.user
            task.save()
        return HttpResponseRedirect(self.success_url)


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Task
    template_name = 'task_update_form.html'
    fields = ['name', 'description', 'status', 'executor']
    success_url = reverse_lazy('tasks_list')
    success_message = 'Task \"%(name)s\" was updated successfully.'


class TaskDeleteView(SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'task_delete_form.html'
    success_url = reverse_lazy('tasks_list')
    success_message = 'Task was deleted successfully.'
