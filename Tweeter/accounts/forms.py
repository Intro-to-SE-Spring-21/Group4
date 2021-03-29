from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from project.models import Comment


# User registration form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # email is required

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

        widgets = {
             'name': forms.TextInput(attrs={'class': 'form-control'}),
             'body': forms.Textarea(attrs={'class': 'form-control'})
        }