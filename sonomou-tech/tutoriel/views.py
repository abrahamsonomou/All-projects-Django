from django.shortcuts import render
from .models import Tutoriel
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)
  
# Create your views here.
def tutoriel(request):
    recent_tutoriels=Tutoriel.objects.order_by('-plublish')[:5]
    list_tutoriel=Tutoriel.objects.all()
    
    paginator=Paginator(list_tutoriel,4)
    page=request.GET.get('page')
    try:
        list_tutoriels=paginator.page(page)
    except PageNotAnInteger:
        list_tutoriels=paginator.page(1)
    except EmptyPage:
        list_tutoriels=paginator.page(paginator.num_pages)
    
    context={
            'tutoriels':list_tutoriels,
            'page':page,
            'recent_tutoriels':recent_tutoriels,
            }
    return render(request,"tutoriel/tutoriel.html",context)

def detail_tutoriel(request,pk:int):
    try:
        tutoriel=Tutoriel.objects.get(pk=pk)
        categorie=tutoriel.categorie
        tutoriel_en_relation=Tutoriel.objects.filter(categorie=categorie)[:5]
        context={
            'tutoriel':tutoriel,
            'tutoriel_en_relation':tutoriel_en_relation,
        }
    except Tutoriel.DoesNotExist:
        raise('This tutoriel doesnot exist')
    return render(request,'tutoriel/detail_tutoriel.html',context)

def search_tutoriel(request):
    query=request.GET["tutoriel"]
    object_list=Tutoriel.objects.filter(titre__icontains=query)
    paginator=Paginator(object_list,6)
    recent_tutoriels=Tutoriel.objects.order_by('-plublish')[:5]

    page=request.GET.get('page')
    try:
        liste_tutoriels=paginator.page(page)
    except PageNotAnInteger:
        liste_tutoriels=paginator.page(1)
    except EmptyPage:
        liste_tutoriels=paginator.page(paginator.num_pages)
    
    context={
            "tutoriels":liste_tutoriels,
            'recent_tutoriels':recent_tutoriels,
            'page':page,
            }
    return render(request,'tutoriel/search_tutoriel.html',context)
