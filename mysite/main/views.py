from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm
from django.contrib import messages
# Create your views here.


def homepage(request):
    if (not request.user.is_authenticated):
        return render(request=request, template_name="main/home.html", context={"user":request.user})

    elif (hasattr(request.user, 'teacher')):
        return render(request=request, template_name="main/home.html", context={"user":request.user, "classes":request.user.teacher.class_set.all()})

    else:
        return render(request=request, template_name="main/home.html", context={"user":request.user, "classes":request.user.student.class_set.all()})

def about(request):
    return render(request=request, template_name="main/about.html")



def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")

    form = SignUpForm
    return render(request=request, template_name="main/register.html", context={"form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")

        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request, "main/login.html", {"form":form})
