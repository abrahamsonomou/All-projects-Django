from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index,name="index"),
    path('/listPermis', listPermis,name="listPermis"),
    path('/addPermis', addPermis,name="addPermis"),
    path('/listVehicule', listVehicule,name="listVehicule"),
    path('/addVehicule', addVehicule,name="addVehicule"),
    path('/listEleve', listEleve,name="listEleve"),
    path('/addEleve', addEleve,name="addEleve"),
    path('/listPaiementEleve', listPaiementEleve,name="listPaiementEleve"),
    path('/addPaiementEleve', addPaiementEleve,name="addPaiementEleve"),
    path('/listMoniteur', listMoniteur,name="listMoniteur"),
    path('/addMoniteur', addMoniteur,name="addMoniteur"),
    path('/listPaiementMoniteur', listPaiementMoniteur,name="listPaiementMoniteur"),
    path('/addPaiementMoniteur', addPaiementMoniteur,name="addPaiementMoniteur"),
    path('/listCours', listCours,name="listCours"),
    path('/addCours', addCours,name="addCours"),
    path('/listLecon', listLecon,name="listLecon"),
    path('/addLecon', addLecon,name="addLecon"),


]
