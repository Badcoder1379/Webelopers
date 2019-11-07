from django.conf.urls import url
from django.contrib.auth.models import *

from home import views

urlpatterns = [
    url('register/', views.register, name="register"),
    url('sign_in/', views.sign_in, name='sign_in'),
    url('login/', views.login, name='login'),
    url('logout/', views.logout_view, name='logout'),
    url('profile/', views.edit_profile_done, name='profile'),
    url('contact_us_done/', views.contact_us_done, name='contact_us_done'),
    url('', views.homePage, name='home'),
]


