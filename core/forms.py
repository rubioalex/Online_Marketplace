from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        # 'placeholder': 'Your Username',
        'class': 'form-field'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        # 'placeholder': 'Your Password',
        'class': 'form-field'
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        # 'placeholder': 'Your Username',
        'class': 'form-field'
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        # 'placeholder': 'Your Email address',
        'class': 'form-field'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        # 'placeholder': 'Your Password',
        'class': 'form-field'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        # 'placeholder': 'Repeat Password',
        'class': 'form-field'
    }))