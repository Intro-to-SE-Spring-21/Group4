from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# User registration form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # email is required

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']