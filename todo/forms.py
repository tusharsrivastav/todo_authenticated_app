from django import forms
from django.forms import ModelForm
from .models import *

class NewTodoForm(forms.Form):
    todo = forms.CharField(label="New todo")

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        widgets = {
        'password': forms.PasswordInput(),
        }
