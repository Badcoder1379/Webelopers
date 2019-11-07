from django.conf.urls import url
from django.urls import path

from home import views

urlpatterns = [
    url('', views.homePage),
    url('register/', views.register),
]
