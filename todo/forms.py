from django import forms
from django.forms import ModelForm
from .models import *

class NewTodoForm(ModelForm):    
    class Meta:
        model = Todo
        fields = ('text',)
        widgets = {
            'text': forms.TextInput(attrs={
                'class': "form-control",
                'style': "width: 300px;",
                'placeholder': "Add a new todo",
            })
        }
        

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        widgets = {
        'password': forms.PasswordInput(),
        }
