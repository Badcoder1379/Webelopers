from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from home.forms import SignUpForm


# Create your views here.


def homePage(request):
    return render(request, 'home.html')


def register(request):
    Error = ''
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        # if form.cleaned_data['pass'] != form.password2:
        #     Error = 'NotEqualPass'
        # users = User.objects.filter(username=form.username)
        # if len(users) != 0:
        #     Error = 'ExistedUser'
        if form.is_valid():
            form.save()
    return render(request, 'register.html', {'form': form})


def sign_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'logged_in.html')
    else:
        return render(request, 'sign_in.html', {'valid': False})
