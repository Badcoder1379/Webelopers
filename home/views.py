from django.shortcuts import render

# Create your views here.


def homePage(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def sign_in(request):
    return render(request, 'sign_in.html')