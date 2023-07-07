from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from .models import *
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

############ Jobforest ################################
def jobforest_home(request):
    return render(request,'jobforest/pages/home.html')

def jobforest_listJob(request):
    return render(request,'jobforest/pages/listJob.html')

def jobforest_listJobDetails(request):
    return render(request,'jobforest/pages/listJobDetails.html')

def jobforest_employers(request):
    return render(request,'jobforest/pages/employers.html')

def jobforest_employersDetails(request):
    return render(request,'jobforest/pages/employersDetails.html')

def jobforest_candidats(request):
    return render(request,'jobforest/pages/candidats.html')

def jobforest_candidatsDetails(request):
    return render(request,'jobforest/pages/candidatsDetails.html')

def jobforest_blog(request):
    return render(request,'jobforest/pages/blog.html')

def jobforest_blogDetails(request):
    return render(request,'jobforest/pages/blogDetails.html')

##################### Parametres du compte ############
def jobforest_profile(request):
    return render(request,'jobforest/pages/dashboard-myprofile.html')

def jobforest_resume(request):
    return render(request,'jobforest/pages/dashboard-myresume.html')

def jobforest_cv_manager(request):
    return render(request,'jobforest/pages/dashboard-cv-manager.html')

def jobforest_appliedjobs(request):
    return render(request,'jobforest/pages/dashboard-appliedjobs.html')

def jobforest_favouritejobs(request):
    return render(request,'jobforest/pages/dashboard-favouritejobs.html')

def jobforest_jobalerts(request):
    return render(request,'jobforest/pages/dashboard-jobalerts.html')

def jobforest_(request):
    return render(request,'jobforest/pages/dashboard-.html')

def jobforest_(request):
    return render(request,'jobforest/pages/dashboard-.html')

def jobforest_(request):
    return render(request,'jobforest/pages/dashboard-.html')

################### Authentification #################
def jobforest_login(request):
    return render(request,'jobforest/auth/login.html')

def jobforest_register(request):
    return render(request,'jobforest/auth/register.html')


################### admin ##########################
def jobforest_dashboard(request):
    return render(request,'jobforest/pages/dashboard.html')

# def jobforest_employers(request):
#     return render(request,'jobforest/pages/home.html')

############ End Jobforest ################################


