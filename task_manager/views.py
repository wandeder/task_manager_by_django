from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth import get_user_model, views, login, logout
from django.urls import reverse_lazy
from task_manager.forms import *
from task_manager.models import user, status, task, label
from django.http import HttpResponseRedirect, HttpResponse
from django.db import models
from django.contrib import messages
from django_filters.views import FilterView
from task_manager.filters import TaskFilter
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy
from task_manager import settings
from django.forms.formsets import formset_factory


def get_error_delete_message(request):
    text_error = _("Can not delete, because this is used")
    return messages.error(request, text_error)


class HomeView(TemplateView):
    model = user
    template_name = 'home.html'


class LoginView(views.LoginView):
    template_name = 'login.html'
    success_message = gettext_lazy('You are log in.')

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        login(self.request, form.get_user())
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.get_success_url())


class LogoutView(views.LogoutView):
    success_message = _('You are log out.')

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return self.get_redirect_url() or self.get_default_redirect_url()


class UsersList(ListView):
    model = user
    context_object_name = 'users_list'
    template_name = 'users_list.html'


class StatusesList(ListView):
    model = status
    context_object_name = 'statuses_list'
    template_name = 'statuses_list.html'


class TaskView(DetailView):
    model = task
    context_object_name = 'task'
    template_name = 'task.html'


class TasksList(FilterView):
    template_name = 'tasks_list.html'
    filterset_class = TaskFilter


class LabelsList(ListView):
    model = label
    context_object_name = 'labels_list'
    template_name = 'labels_list.html'


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'create_form.html'
    success_url = reverse_lazy('login')
    extra_context = {'button': _('Registrate')}
    success_message = _('Your account has been successfully created.')


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = user
    fields = ['username', 'first_name', 'last_name', 'email', ]
    template_name = 'update_form.html'
    success_url = reverse_lazy('users_list')
    extra_context = {
        'password_form': PasswordUpdateForm(user),
        'user_update': True,
    }
    success_message = _('Your account has been successfully updated.')


class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = user
    template_name = 'delete_form.html'
    success_url = reverse_lazy('users_list')
    success_message = _('Your account has been successfully deleted.')

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except models.ProtectedError:
            get_error_delete_message(self.request)
            return HttpResponseRedirect(success_url)
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(success_url)


class StatusCreateView(SuccessMessageMixin, CreateView):
    form_class = StatusCreationForm
    template_name = 'create_form.html'
    success_url = reverse_lazy('statuses_list')
    success_message = _('Status was created successfully.')


class StatusUpdateView(SuccessMessageMixin, UpdateView):
    model = status
    template_name = 'update_form.html'
    fields = ['name', ]
    extra_context = {'title': _('status')}
    success_url = reverse_lazy('statuses_list')
    success_message = 'Status was updated successfully.'


class StatusDeleteView(SuccessMessageMixin, DeleteView):
    model = status
    template_name = 'delete_form.html'
    extra_context = {'title': _('status')}
    success_url = reverse_lazy('statuses_list')
    success_message = 'Status was deleted successfully.'

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except models.ProtectedError:
            get_error_delete_message(self.request)
            return HttpResponseRedirect(success_url)
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(success_url)


class TaskCreateView(SuccessMessageMixin, CreateView):
    form_class = TaskCreationForm
    template_name = 'create_form.html'
    success_url = reverse_lazy('tasks_list')
    success_message = _('Task was created successfully.')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.creator = request.user
            task.save()
            form.save_m2m()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.success_url)


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = task
    template_name = 'update_form.html'
    extra_context = {'title': _('task')}
    fields = ['name', 'description', 'status', 'executor', 'labels']
    success_url = reverse_lazy('tasks_list')
    success_message = _('Task was updated successfully.')


class TaskDeleteView(SuccessMessageMixin, DeleteView):
    model = task
    template_name = 'delete_form.html'
    extra_context = {'title': _('task')}
    success_url = reverse_lazy('tasks_list')
    success_message = _('Task was deleted successfully.')


class LabelCreateView(SuccessMessageMixin, CreateView):
    form_class = LabelCreationForm
    template_name = 'create_form.html'
    success_url = reverse_lazy('labels_list')
    success_message = _('Label was created successfully.')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            label = form.save(commit=False)
            label.creator = request.user
            label.save()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.success_url)


class LabelUpdateView(SuccessMessageMixin, UpdateView):
    model = label
    template_name = 'update_form.html'
    fields = ['name', ]
    extra_context = {'title': _('label')}
    success_url = reverse_lazy('labels_list')
    success_message = _('Label was updated successfully.')


class LabelDeleteView(SuccessMessageMixin, DeleteView):
    model = label
    template_name = 'delete_form.html'
    extra_context = {'title': _('label')}
    success_url = reverse_lazy('labels_list')
    success_message = _('Label was deleted successfully.')

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except models.ProtectedError:
            get_error_delete_message(self.request)
            return HttpResponseRedirect(success_url)
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(success_url)
