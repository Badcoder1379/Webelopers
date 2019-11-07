from django.conf.urls import url
from django.urls import path

from home import views

urlpatterns = [
    url('register/', views.register),
    url('', views.homePage)
]
