from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("signup/", views.signup_page, name="signup_page"),
    path("login/", views.login_page, name="login_page"),
]

