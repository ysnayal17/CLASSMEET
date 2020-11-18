from django.shortcuts import render, redirect
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


# User: username-Harry Password-HarryBhaii

# Create your views here.
def loginUser(request):
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
            print(request)
            return render(request, 'login.html')

    else:
        return render(request, "login.html")

def logoutUser(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect("/login")

def home(request):
    # return HttpResponse("Hello World")
    # messages.success(request, 'Hey You are in Home Page')
    print(request.user)
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
    return render(request, "academics_sm.html")

def academics_vr(request):
    return render(request, "academics_vr.html")

def academics_q(request):
    return render(request, "academics_q.html")

def academics_a(request):
    return render(request, "academics_a.html")

