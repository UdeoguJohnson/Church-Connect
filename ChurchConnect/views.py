from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

def home_page(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')



