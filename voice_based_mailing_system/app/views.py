from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'')

def login_view(request):
    return render(request, 'app/login.html')
