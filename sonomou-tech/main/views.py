from django.shortcuts import render
from .models import *
from blog.models import Article

# Create your views here.
def index(request):
    list_sliders=Slider.objects.all().filter(status=True)
    list_temoingnages=Temoignage.objects.all().filter(status=True)
    list_articles=Article.objects.filter(statut=True).order_by('-updated')[:3]


    context={
        'articles':list_articles,
        'list_temoingnages':list_temoingnages,
        'list_sliders':list_sliders,
        }
    return render(request,"pages/index.html",context)
 
 
 
 
 
 
 
   
# gestion des erreurs
def handler403(request,exception):
    return render(request,'pages/403.html')

def handler404(request, exception):
    return render(request,'pages/404.html',status=404)

def handler500(request):
    return render(request,'pages/500.html')

def handler503(request,exception):
    return render(request,'pages/503.html') 