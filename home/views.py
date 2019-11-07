from django.shortcuts import render, redirect

from home.forms import UserCreationForm

# Create your views here.


def homePage(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        form.save()
    return render(request, 'register.html')



def sign_in(request):
    return render(request, 'sign_in.html')
