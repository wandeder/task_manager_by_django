"""todos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from task_manager.views import HomeView, UserCreateView, UsersList, UserCreateDoneView, UserUpdateView, UserUpdateDoneView, UserDeleteView, UserDeleteDoneView, StatusesList, StatusCreateView, StatusUpdateView, StatusDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('users/', UsersList.as_view(), name='users_list'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/create/done', UserCreateDoneView.as_view(), name='user_create_done'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/int:pk>/update/done', UserUpdateDoneView.as_view(), name='user_update_done'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('users/int:pk>/delete/done', UserDeleteDoneView.as_view(), name='user_delete_done'),
    path('statuses', StatusesList.as_view(), name='statuses_list'),
    path('statuses/create/', StatusCreateView.as_view(), name='status_create'),
    path('statuses/<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
    path('statuses/<int:pk>/delete/', StatusDeleteView.as_view(), name='statuses_delete'),
]
