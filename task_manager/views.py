from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from task_manager.forms import UserCreationForm


User = get_user_model()

class HomeView(TemplateView):
    model = User
    template_name = 'home.html'


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'user_create_form.html'
    success_url = reverse_lazy('user_create_done')


class UserCreateDoneView(TemplateView):
    model = User
    template_name = 'user_create_done.html'


class UserUpdateView(UpdateView):
    model = User
    template_name = 'user_update_form.html'
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy('user_update_done')


class UserUpdateDoneView(TemplateView):
    model = User
    template_name = 'user_update_done.html'


class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_delete_form.html'
    success_url = reverse_lazy('user_delete_done')


class UsersList(ListView):
    model = User
    context_object_name = 'users_list'
    template_name = 'users_list.html'


class UserDeleteDoneView(TemplateView):
    model = User
    template_name = 'user_delete_done.html'
