from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from task_manager.models import user

admin.site.register(user, UserAdmin)
