from django.conf.urls import url
from django.contrib.auth.models import *


from home import views

urlpatterns = [
    url('register/', views.register, name="register"),
    url('sign_in/', views.sign_in, name='sign_in'),
    url('', views.homePage, name='home'),
]
