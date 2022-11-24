from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from task_manager.forms import *
from task_manager.models import Status, Task, Label
from django.http import HttpResponseRedirect
from django.db import models
from django.contrib import messages
from django_filters.views import FilterView
from task_manager.filters import TaskFilter


User = get_user_model()


def get_error_delete_message(request, extra_context):
    text_error = f"Can not delete, because this {extra_context.get('title')} is used"
    return messages.error(request, text_error)


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


class TaskView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task.html'


class TasksList(FilterView):
    template_name = 'tasks_list.html'
    filterset_class = TaskFilter


class LabelsList(ListView):
    model = Label
    context_object_name = 'labels_list'
    template_name = 'labels_list.html'


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'create_form.html'
    success_url = reverse_lazy('login')
    success_message = '\"%(username)s\" your account has been successfully created.'


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'update_form.html'
    extra_context = {'title': 'user'}
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy('users_list')
    success_message = '\"%(username)s\" your account has been successfully updated.'


class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'delete_form.html'
    extra_context = {'title': 'user'}
    success_url = reverse_lazy('users_list')
    success_message = 'Your account has been successfully deleted.'

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except models.ProtectedError:
            get_error_delete_message(self.request, self.extra_context)
            return HttpResponseRedirect(success_url)
        return HttpResponseRedirect(success_url)


class StatusCreateView(SuccessMessageMixin, CreateView):
    form_class = StatusCreationForm
    template_name = 'create_form.html'
    success_url = reverse_lazy('statuses_list')
    success_message = 'Status \"%(name)s\" was created successfully.'


class StatusUpdateView(SuccessMessageMixin, UpdateView):
    model = Status
    template_name = 'update_form.html'
    fields = ['name', ]
    extra_context = {'title': 'status'}
    success_url = reverse_lazy('statuses_list')
    success_message = 'Status \"%(name)s\" was updated successfully.'


class StatusDeleteView(SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'delete_form.html'
    extra_context = {'title': 'status'}
    success_url = reverse_lazy('statuses_list')
    success_message = 'Status was deleted successfully.'

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except models.ProtectedError:
            get_error_delete_message(self.request, self.extra_context)
            return HttpResponseRedirect(success_url)
        return HttpResponseRedirect(success_url)


class TaskCreateView(SuccessMessageMixin, CreateView):
    form_class = TaskCreationForm
    template_name = 'create_form.html'
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
    template_name = 'update_form.html'
    extra_context = {'title': 'task'}
    fields = ['name', 'description', 'status', 'executor', 'labels']
    success_url = reverse_lazy('tasks_list')
    success_message = 'Task \"%(name)s\" was updated successfully.'


class TaskDeleteView(SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'delete_form.html'
    extra_context = {'title': 'task'}
    success_url = reverse_lazy('tasks_list')
    success_message = 'Task was deleted successfully.'


class LabelCreateView(SuccessMessageMixin, CreateView):
    form_class = LabelCreationForm
    template_name = 'create_form.html'
    success_url = reverse_lazy('labels_list')
    success_message = 'Label \"%(name)s\" was created successfully.'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            label = form.save(commit=False)
            label.creator = request.user
            label.save()
        return HttpResponseRedirect(self.success_url)


class LabelUpdateView(SuccessMessageMixin, UpdateView):
    model = Label
    template_name = 'update_form.html'
    fields = ['name', ]
    extra_context = {'title': 'label'}
    success_url = reverse_lazy('labels_list')
    success_message = 'Label \"%(name)s\" was updated successfully.'


class LabelDeleteView(SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'delete_form.html'
    extra_context = {'title': 'label'}
    success_url = reverse_lazy('labels_list')
    success_message = 'Label was deleted successfully.'

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except models.ProtectedError:
            get_error_delete_message(self.request, self.extra_context)
            return HttpResponseRedirect(success_url)
        return HttpResponseRedirect(success_url)
