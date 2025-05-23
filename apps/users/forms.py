from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_business', 'nip', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    pass
