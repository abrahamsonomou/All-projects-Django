from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import CustomerUser


# Create your views here.
def login_user(request):
    if request.method== "POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            
            #user=authenticate(username=username,password=password)
            user=CustomerUser.objects.filter(username=username).first()
            if user and check_password(password, user.password):
                print(user)
                if user is not None:
                    #users=CustomerUser.objects.filter(username=username).first()
                    if not user.is_active:
                        messages.error(request,"Votre compte n'est pas activé, veuillez contacter l'administrateur")
                        return render(request,"pages/login.html",{"form":form})
                    
                    login(request,user)
                    return redirect('index')
            else:
                messages.error(request,"Autehtification echouee. Vos informations sont incorrectes")
                return render(request,"pages/login.html",{"form":form})
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class']+= ' is-invalid'
            return render(request,"pages/login.html",{"form":form})
    else:
        form=LoginForm()
    return render(request,"pages/login.html",{"form":form})
    
def register_user(request):
    if request.method== "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            last_name=form.cleaned_data['last_name']
            first_name=form.cleaned_data['first_name']
            password_confirm=form.cleaned_data['password_confirm']
            print(last_name,first_name) 
            if password != password_confirm:
                messages.error(request,'Mot de passe non identique')
                return render(request,'pages/register.html',{'form':form})
            else:
                user=CustomerUser.objects.filter(username=username).first()
                if user is not None:
                    messages.error(request,'Ce nom d''utilisateur existe')
                    return render(request,'pages/register.html',{'form':form})
                else:
                    userEmail=CustomerUser.objects.filter(email=email).first()
                    if userEmail is not None:
                        messages.error(request,'Cet email existe')
                        return render(request,'pages/register.html',{'form':form})
                    else:
                        user=CustomerUser.objects.create_user(email=email,username=username,password=password,last_name=last_name,first_name=first_name)
                        if user is not None:
                            login(request,user)
                            return redirect('login')
                        else:
                            messages.error(request,'Creation de compte echouee')
                            return render(request,'pages/register.html',{'form':form})
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class']+= ' is-invalid'
            return render(request,"pages/register.html",{"form":form})
    else:
        form=RegisterForm(request.POST)
    return render(request,"pages/register.html",{"form":form})

def forgot_password(request):
    return render(request,"pages/forgot_password.html")

def logout_user(request):
    logout(request)
    return redirect('login')

