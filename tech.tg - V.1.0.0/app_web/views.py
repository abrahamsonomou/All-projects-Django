from tkinter.messagebox import NO
from django.shortcuts import render,get_list_or_404
from .models import *
from  app_formation.models import *
from .forms import *
from django.shortcuts import redirect, render
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)
from django.contrib import messages

# Create your views here.

def index(request):
    list_services=Service.objects.order_by('-updated')[:6]
    list_teams=Team.objects.all()
    list_sliders=Slider.objects.all()
    list_temoingnages=Temoignage.objects.all()
    nb_articles=Article.objects.count()
    nb_team=Team.objects.count()
    nb_temoignage=Temoignage.objects.count()
    nb_service=Service.objects.count()
    list_articles=Article.objects.order_by('-created')[:3]


    context={
        'list_services':list_services,
        'list_teams':list_teams,
        'list_articles':list_articles,
        'list_temoingnages':list_temoingnages,
        'list_sliders':list_sliders,
        'nb_articles':nb_articles,
        'nb_team':nb_team,
        'nb_temoignage':nb_temoignage,
        'nb_service':nb_service,
        }
    return render(request,"pages/index.html",context)


def about(request):
    return render(request,"pages/about.html")

def team(request):
    list_teams=Team.objects.all()
    nb_team=Team.objects.count()
    context={
    'list_teams':list_teams,
    'nb_team':nb_team,
        }
    return render(request,"pages/team.html",context)

def blog(request):
    recent_articles=Article.objects.order_by('-created')[:5]
    list_articles=Article.objects.all()
    
    paginator=Paginator(list_articles,4)
    page=request.GET.get('page')
    try:
        articles=paginator.page(page)
    except PageNotAnInteger:
        articles=paginator.page(1)
    except EmptyPage:
        articles=paginator.page(paginator.num_pages)
    
    context={
            'articles':articles,
            'page':page,
            'recent_articles':recent_articles,
            }
    return render(request,"pages/blog.html",context)

def detail_article(request,slug:str):
    try:
        article=Article.objects.get(slug=slug)
        categorie=article.categorie
        article_en_relation=Article.objects.filter(categorie=categorie)[:5]
        context={
            'aer':article_en_relation,
            'article':article,
        }
    except Article.DoesNotExist:
        raise('This article doesnot exist')
    return render(request,'pages/detail_article.html',context)

def search_article(request):
    query=request.GET["article"]
    object_list=Article.objects.filter(titre__icontains=query)
    paginator=Paginator(object_list,12)
    recent_articles=Article.objects.order_by('-created')[:5]

    page=request.GET.get('page')
    try:
        liste_article=paginator.page(page)
    except PageNotAnInteger:
        liste_article=paginator.page(1)
    except EmptyPage:
        liste_article=paginator.page(paginator.num_pages)
    
    context={
            "liste_article":liste_article,
            'recent_articles':recent_articles,
            'page':page,
            }
    return render(request,'pages/search_article.html',context)


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
            'list_tutoriels':list_tutoriels,
            'page':page,
            'recent_tutoriels':recent_tutoriels,
            }
    return render(request,"pages/tutoriel.html",context)

def detail_tutoriel(request,slug:str):
    try:
        tutoriel=Tutoriel.objects.get(slug=slug)
        context={
            'tutoriel':tutoriel,
        }
    except Tutoriel.DoesNotExist:
        raise('This tutoriel doesnot exist')
    return render(request,'pages/detail_tutoriel.html',context)

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
            "liste_tutoriels":liste_tutoriels,
            'recent_tutoriels':recent_tutoriels,
            'page':page,
            }
    return render(request,'pages/search_tutoriel.html',context)


def formations(request):
    list_formation=Formation.objects.all()
    
    paginator=Paginator(list_formation,12)
    page=request.GET.get('page')
    try:
        list_formations=paginator.page(page)
    except PageNotAnInteger:
        list_formations=paginator.page(1)
    except EmptyPage:
        list_formations=paginator.page(paginator.num_pages)
    
    context={
            'list_formations':list_formations,
            }
    return render(request,"pages/formations.html",context)

def detail_formations(request,slug:str):

    try:
        formation=Formation.objects.get(slug=slug)
        categorie=formation.categorie
        formations_en_relation=Formation.objects.filter(categorie=categorie)[:5]
        context={
            'formation':formation,
            'formations_en_relation':formations_en_relation,
        }
    except Tutoriel.DoesNotExist:
        raise('This formation doesnot exist')
    return render(request,'pages/detail_formations.html',context)

def search_formations(request):
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
            "liste_tutoriels":liste_tutoriels,
            'recent_tutoriels':recent_tutoriels,
            'page':page,
            }
    return render(request,'pages/search_tutoriel.html',context)

class Contact(CreateView):
    model=Contact
    form_class=ContactForm
    template_name='pages/contact.html'
    success_url='/'
    
# class NewLetter(CreateView):
#     model=NewsLetter
#     form_class=NewLetterForm()
#     template_name='pages/contact.html'
#     success_url='/'

def newletter(request):
    form=NewLetterForm(request.POST)
    if form.is_valid():
        instance=form.save(commit=False)
        if NewsLetter.objects.filter(email=instance.email).exists():
            messages.warning(request,
            "Désolé! Cet email existe dans la base de données",
            "alert alert-danger alert-dismissible")
        else:
            instance.save()
            messages.success(request,
            "Merci pour votre abonnement",
            "alert alert-success alert-dismissible")
            
    context={
        'form':form,
        }
    return render(request,"pages/index.html",context)
    # return render(request,"pages/newletter.html",context)

def newLetter_unsubscribe(request):
    form=NewLetterForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        if NewsLetter.objects.filter(email=instance.email).exists():
            NewsLetter.objects.filter(email=instance.email).delete()
            messages.success(request,
            "Vous-vous est désabonné",
            "alert alert-success alert-dismissible")
        else:
            messages.warning(request,
            "Désolé! Cet email n'existe pas dans la base de données",
            "alert alert-danger alert-dismissible")
