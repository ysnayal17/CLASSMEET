from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    # return HttpResponse("Hello World")
    # messages.success(request, 'Hey You are in Home Page')
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

