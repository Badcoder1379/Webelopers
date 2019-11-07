from django.conf.urls import url
from django.urls import path

from home import views

urlpatterns = [
    url('register/', views.register, name="register"),

    url('', views.homePage, name="home"),
]
