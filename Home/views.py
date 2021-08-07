from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from datetime import datetime
from Home.models import Contact
from Home.models import StudyMaterials
from Home.models import Questions
from Home.models import Answers
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import CoursePackForm

# User: username-Harry Password-HarryBhaii

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg', 'mp4', 'pdf']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg', 'gif']


def login_user(request):
    # return HttpResponse("Hello World")
    # messages.success(request, 'Hey You are in Home Page')
    if request.method == 'POST':
        username = request.POST.get('LoginUsername')
        password = request.POST.get('LoginPass')
        print(username, password)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect("/home")
        else:
            messages.error(request, "Pls try again")
            return render(request, 'login.html')

    else:
        return render(request, "login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect("/login")


def home(request):
    # return HttpResponse("Hello World")
    # messages.success(request, 'Hey You are in Home Page')
    # print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, "home.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'You have contacted successfully')
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def faq(request):
    return render(request, "faq.html")


def academics_sm(request):
    if request.user.is_anonymous:
        messages.error(request, 'You should login first')
        return redirect("/login")
    else:
        form = CoursePackForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user
            course.thumbnail = request.FILES['thumbnail']
            file_type = course.thumbnail.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'course': course,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'Home/create_coursepack.html', context)
            course.save()
            return render(request, 'Home/detail.html', {'course': course})
        context = {
            "form": form,
        }
        return render(request, 'lecture/create_coursepack.html', context)


def academics_vr(request):
    if request.user.is_anonymous:
        messages.error(request, 'You should login first')
        return redirect("/login")

    return render(request, "academics_vr.html")


def signup_user(request):
    if request.method == "POST":
        username = request.POST['SignupUsername']
        email = request.POST['SignupEmail']
        pass1 = request.POST['SignupPass1']
        pass2 = request.POST['SignupPass2']
        if pass1 == pass2:
            new_user = User.objects.create_user(username, email, pass1)
            new_user.save()
            messages.success(request, "Successfully created your account!!")
            return render(request, "home.html")
        else:
            messages.error(request, "Check Your Password Again")
            return redirect("/login")
    else:
        return HttpResponse(request, "404 - Page not found")


# def get_name(request):
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/thanks/')
#     else:
#         form = NameForm()
#
#     return render(request, 'academics_sm.html', {'form': form})
