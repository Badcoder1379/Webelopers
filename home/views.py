from django.shortcuts import render

from home.forms import SignUpForm


# Create your views here.


def homePage(request):
    return render(request, 'home.html', {'login': False})


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        form.save()
    return render(request, 'register.html')


def sign_in(request):
    return render(request, 'sign_in.html')


def contact_us_done(request):
    return render(request, 'contact_us_done.html')
