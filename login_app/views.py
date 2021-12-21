from django import forms
from django.forms import ModelForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.checks import messages
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.hashers import make_password
from login_app.models import CreateUser
from login_app.forms import CreateFrom, LoginFrom , EditForm


# Create your views here.
def index(request):
    return render(request, 'login_app/home.html')


def update_user_view(request):
    if request.method == 'POST':
        single_user = get_object_or_404(CreateUser, id=id)
        frm = EditForm(request.POST, instance=single_user)
        if frm.is_valid():
            frm.save()
            messages.message(request, 'hi! {0} your profile is updated'.format(single_user))
            return redirect('YouTube_DownApp:home_page')
    else:
        single_user=get_object_or_404(CreateUser, id=id)
        frm = EditForm(instance=single_user)
    return render(request, 'ytd_app/home.html', {'single_user': single_user, 'form': frm})


#view for user registation
def reg_user(request):
    if request.method == 'POST':
        frm = CreateFrom(request.POST, request.FILES)
        if frm.is_valid():
            full_name = frm.cleaned_data.get('full_name')
            image = frm.cleaned_data.get('image')
            user_name = frm.cleaned_data.get('user_name')
            email = frm.cleaned_data.get('email')
            password1 = frm.cleaned_data.get('password1')
            password2 = frm.cleaned_data.get('password2')

            if User.objects.filter(user_name=user_name).exists():
                messages.error(request, 'Sorry {0} is already exists'.format(user_name))
                return redirect('login_app:signup')
            else:
                if password1 != password2:
                    messages.error(request, "Oops! password doesn't match!")
                    return redirect('login_app:signup')
                else:
                    password_hash = make_password(password2)
                    user = User.objects.create(
                        user_name=user_name, password=password_hash, email=email
                    )

                    new_user = CreateUser()
                    new_user.user = user
                    new_user.full_name = full_name
                    new_user.image = image
                    new_user.save()

                    messages.success(
                        request, 'Congratulations {0} your account has been craated successfully'.format(user)
                        )
                    return redirect('login_app:signin')
    else:
        frm= CreateFrom()
    return render(request, 'login_app/signUp.html', {'form':frm})


#view of signin view
def signin_view(request):
    if not request.user.is_authenticated:
        frm = LoginFrom()
        if request.method == 'POST':
            frm = LoginFrom(request.POST)
            if frm.is_valid():
                user_name = frm.cleaned_data['user_name']
                password = frm.cleaned_data['password']
                user = authenticate(user_name=user_name, password=password)
                if user:
                    login(request, user)
                    messages.success(request, 'Hi, your Video Downloaded successfull')
                    return redirect('login_app:index')
                else:
                    messages.error(request, 'Oops! your login failed')
        return render(request, 'login_app/signin.html', {'form':frm})
    else:
        return redirect('login_app:signin')


#sign out view
def signout_view(request):
    logout(request)
    messages.success(request, 'You just logged Out')
    return redirect('login_app:signin')
    
