from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django import forms


def new(request):
    return render(request, "new.html",
                  {"lifts": get_user_lifts(request)})


def index(request):
    if request.user.is_anonymous:
        return HttpResponse(
            """<div><a href="/login">Login</a> or <a href="sign_in">register.</a> </div>""")
    return render(request, "index.html",
                  {"sessions": get_user_sessions(request)})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == "" or password == "":
            return HttpResponse("Please fill in all required fields")
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse("Unauthorized!")
        else:
            login(request, user)
            return redirect('/')
    return render(request, "login.html")


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if username == "" or password == "" or email == "":
            return HttpResponse("Please fill in all required fields")
        User.objects.create_user(username=username, password=password, email=email)
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse("Unauthorized!")
        else:
            login(request, user)
            return redirect('LiftoffApp/')
    return render(request, "sign_in.html")


def username(request):
    return HttpResponse(request.user.username)


def logout_user(request):
    logout(request)
    return redirect('LiftoffApp/')
