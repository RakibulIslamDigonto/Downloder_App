from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import CreateUser


class CreateFrom(forms.Form):
    full_name = forms.CharField(label='Full Name', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Name'}))

    user_name = forms.CharField(label='Username', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Name'}))

    email = forms.EmailField(label='Email', required=False, widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'example@email.com'}))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))

    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    image = forms.ImageField(label='image', required=False)


class LoginFrom(forms.Form):
    user_name = forms.CharField(label='User Name', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':'Enter your User name'}))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))


class EditForm(forms.ModelForm):
    full_name =  forms.CharField(label='Full Name', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your Name'}))

    image = forms.ImageField(label='image', required=False)
    class Meta:
        model = CreateUser()
        fields = ['full_name', 'image']

