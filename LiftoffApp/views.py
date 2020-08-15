from .models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from .forms import FormSessionPlan


def new(request):
    form = FormSessionPlan(request)
    if request.method == 'POST':
        existing_lifts = {lift: (get_last_weight(lift, request.user)[0],
                                 get_set_values_per_last_lift(lift, request.user))
                          for lift
                          in request.POST.getlist('choices')}
        added_lifts = dict(zip(request.POST.getlist('newlift[]'),
                               request.POST.getlist('startweight[]')))
        for k,v in added_lifts.items():
            added_lifts[k] = (v, [0,0,0,0,0])

        added_lifts.update(existing_lifts)
        data = added_lifts
        print(data)
    return render(request, "new.html",
                  {"lifts": get_user_lifts_unique(request),
                   "form": form})


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
