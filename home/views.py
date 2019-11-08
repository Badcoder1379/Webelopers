from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from home.forms import SignUpForm


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
            return redirect("/")
        else:
            return render(request, 'sign_in.html',
                          {'valid': False, 'register_button': True, 'sign_in_button': True, 'exit_button': False})
    return render(request, 'sign_in.html', {'valid': True})


def contact_us_done(request):
    return render(request, 'contact_us_done.html',
                  {'register_button': True, 'sign_in_button': True, 'exit_button': False})


def login_view(request):
    return render(request, 'logged_in.html',
                  {'register_button': False, 'sign_in_button': False, 'exit_button': True})


def logout_view(request):
    logout(request)
    return redirect("/")


def edit_profile_done(request):
    if request.POST:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if first_name != "":
            request.user.first_name = first_name
        if last_name != "":
            request.user.last_name = last_name
    return render(request, 'profile.html')


def edit_profile(request):
    return render(request, 'edit_profile.html')


def load_panel(request):
    return render(request, 'panel.html')