from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request,'pages/register.html')


def login(request):
    return render(request,'pages/login.html')

def logout(request):
    return render(request,'pages/login.html')
