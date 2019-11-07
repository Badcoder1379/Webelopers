from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from home.forms import SignUpForm


# Create your views here.


def homePage(request):
    return render(request, 'home.html', {'register_button': True, 'sign_in_button': True, 'exit_button': False})


def register(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'register.html',
                  {'form': form, 'register_button': True, 'sign_in_button': True, 'exit_button': False})


def sign_in(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'logged_in.html',
                          {'register_button': False, 'sign_in_button': False, 'exit_button': True})
        else:
            return render(request, 'sign_in.html',
                          {'valid': False, 'register_button': True, 'sign_in_button': True, 'exit_button': False})
    return render(request, 'sign_in.html',
                  {'valid': True, 'register_button': True, 'sign_in_button': True, 'exit_button': False})


def contact_us_done(request):
    return render(request, 'contact_us_done.html',
                  {'register_button': True, 'sign_in_button': True, 'exit_button': False})
