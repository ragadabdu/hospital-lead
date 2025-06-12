from django.contrib.auth.forms import UserCreationForm
from .models import Receptionist

class SimpleRegistrationForm(UserCreationForm):
    class Meta:
        model = Receptionist
        fields = ['username', 'password1', 'password2']