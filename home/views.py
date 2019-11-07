from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.




def homePage(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        form.save()
    return render(request, 'home.html')


def register(request):
    return render(request, 'register.html')

def sign_in(request):
    return render(request, 'sign_in.html')