from django.shortcuts import render
from permis.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request,'pages/home.html',locals())

def listPermis(request):
    list_permis=Permis.objects.all()
    context={
        'permis':list_permis
    }
    return render(request,'pages/listPermis.html',context)
  
def addPermis(request):
    return render(request,'pages/addPermis.html',locals())

def listVehicule(request):
    return render(request,'pages/listVehicule.html',locals())

def addVehicule(request):
    return render(request,'pages/addVehicule.html',locals())

def listLecon(request):
    return render(request,'pages/listLecon.html',locals())

def addLecon(request):
    return render(request,'pages/addLecon.html',locals())

def listEleve(request):
    return render(request,'pages/listEleve.html',locals())

def addEleve(request):
    return render(request,'pages/addEleve.html',locals())

def listMoniteur(request):
    return render(request,'pages/listMoniteur.html',locals())

def addMoniteur(request):
    return render(request,'pages/addMoniteur.html',locals())

def listPaiementEleve(request):
    return render(request,'pages/listPaiementEleve.html',locals())

def addPaiementEleve(request):
    return render(request,'pages/addPaiementEleve.html',locals())

def listPaiementMoniteur(request):
    return render(request,'pages/listPaiementMoniteur.html',locals())

def addPaiementMoniteur(request):
    return render(request,'pages/addPaiementMoniteur.html',locals())


def listCours(request):
    return render(request,'pages/listCours.html',locals())


def addCours(request):
    return render(request,'pages/addCours.html',locals())


# def (request):
#     return render(request,'pages/.html',locals())