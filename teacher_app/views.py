from django.shortcuts import render, redirect
from IELTS_eLearning_frontend.localsettings import url
from django.contrib import messages
import requests

# Create your views here.
# def home(request):
#     return render(request, 'index.html')


# def login(request):
#     return render(request, 'login.html')

# def logout(request):
#     return render(request, 'logout.html')

# def profile(request):
#     return render(request, 'profile.html')

def courses(request):
    return render(request, 'courses.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def team (request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def four04(request):
    return render(request, '404.html')