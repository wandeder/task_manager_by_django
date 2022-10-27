from django.contrib.auth.forms import UserCreationForm
from task_manager.models import User

class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        #fields = ['first_name', 'last_name', 'email',] 
