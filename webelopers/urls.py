"""webelopers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('register/', views.register, name="register"),
    url('sign_in/', views.sign_in, name='sign_in'),
    url('login/', views.login, name='login'),
    url('edit_profile', views.edit_profile, name='edit_profile'),
    url('logout/', views.logout_view, name='logout'),
    url('profile/', views.edit_profile_done, name='profile'),
    url('contact_us_done/', views.contact_us_done, name='contact_us_done'),
    url('', views.homePage, name='home'),
]
