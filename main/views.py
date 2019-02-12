from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, JoinClassForm, AssignmentForm
from django.contrib import messages
from .models import Class
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from base64 import decodestring
import base64
from io import BytesIO
# Create your views here.


def homepage(request):
    if (request.method == "POST"):
        form = JoinClassForm(request.POST)
        if (form.is_valid()):
            enrolled = False
            for c in Class.objects.all():
                code = form.cleaned_data.get("join_code")
                if (c.class_code == code):
                    request.user.student.class_set.add(c) # add the student to the class
                    messages.success(request, f"You are now enrolled in {c.name}")
                    enrolled = True
            if not enrolled:
                messages.error(request, f"We could not find a class with Join Code {code}.")
        return redirect("main:homepage")




    if (not request.user.is_authenticated):
        return render(request=request, template_name="main/home.html", context={"user":request.user})

    elif (hasattr(request.user, 'teacher')):
        return render(request=request, template_name="main/home.html", context={"user":request.user, "classes":request.user.teacher.class_set.all()})

    else:
        form = JoinClassForm()
        return render(request=request, template_name="main/home.html", context={"user":request.user, "classes":request.user.student.class_set.all(), "form":form})

def about(request):
    return render(request=request, template_name="main/about.html")

def new_assignment(request):
    if (request.method == "POST"):
        return HttpResponse("Success!")

    form = AssignmentForm()
    return render(request=request, template_name="main/new_assignment.html", context={"user":request.user, "form":form})

@csrf_exempt
def add_interest(request):
    if (request.method == "POST"):
        interest = request.POST["interest"]
        return HttpResponse("Success!")

@csrf_exempt
def get_handwritten(request):
    if (request.method == "POST"):
        image = request.POST["imgBase64"]
        print(image)
        # im = Image.open(BytesIO(base64.b64decode(image)))
        # im.save("im.jpeg")
        with open("imageToSave.jpeg", "wb") as fh:
            fh.write(base64.b64decode(image.replace("data:image/jpeg;base64,", "")))
        return HttpResponse("Success!")




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
