from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url="login_page")
def homepage(request):
    return render(request, "home.html")

def signup_page(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password")
        pass2 = request.POST.get("confirm-password")
        if pass1 != pass2:
            return HttpResponse("Passwords should be the same")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect("login_page")
    return render(request, "signup.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("password")
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            return HttpResponse("Invalid credentials")
    return render(request, "login.html")

def Logout_page(request):
    logout(request)
    return redirect("login_page")
