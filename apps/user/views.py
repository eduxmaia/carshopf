from django.shortcuts import render
from .models import User

# Create your views here.

def login(request):
    return render(request, 'login/login.html')

def username(request):
    users = User.objects.all()

    context = {
        'users': users
    }
    return render(request, 'core/home.html', context)