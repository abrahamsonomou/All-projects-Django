from django.shortcuts import redirect,render,get_list_or_404
from .models import *
from .forms import *
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)
from django.contrib import messages
from django.core import mail
from django.conf import settings
from django.views.generic.edit import CreateView

# Create your views here.

def index(request):
    list_services=Service.objects.order_by('-updated')[:6]
    list_teams=Team.objects.all()
    list_temoingnages=Temoignage.objects.all()
    list_articles=Article.objects.order_by('-updated')[:4]


    context={
        'list_services':list_services,
        'list_teams':list_teams,
        'list_articles':list_articles,
        'list_temoingnages':list_temoingnages,
        }
    return render(request,"pages/index.html",context)

def about(request):
    return render(request,"pages/about.html")

def service(request):
    list_services=Service.objects.all()
    list_temoingnages=Temoignage.objects.all()
    
    context={
    'list_services':list_services,
    'list_temoingnages':list_temoingnages,
        }
    return render(request,"pages/service.html",context)

class Contact(CreateView):
    model=Contact
    form_class=ContactForm
    template_name='pages/contact.html'
    success_url='blog'

# def contact(request):
#     form=ContactForm(request.POST)
#     if form.is_valid():
#         instance=form.save(commit=False)
#         if Contact.objects.filter(email=instance.email).exists():
#             messages.warning(request,
#             "Désolé! Cet email existe dans la base de données",
#             "alert alert-danger alert-dismissible")
            
#         else:
#             instance.save()
#             messages.success(request,
#             "Nous avons réçu votre message !",
#             "alert alert-success alert-dismissible")
            # connection = mail.get_connection()
            # nom=form.cleaned_data['nom']
            # email=form.cleaned_data['email']
            # sujet=form.cleaned_data['sujet']
            # message=form.cleaned_data['message']
            # email1 = mail.EmailMessage(
            # sujet,
            # message,
            # settings.DEFAULT_FROM_EMAIL,
            # [email],
            # connection=connection,
            # )
            
            # email1.send() 
            
            # connection.close()
            
    # context={
    #     'form':form,
    #     }
    # return render(request,"pages/contact.html",context)


def team(request):
    list_teams=Team.objects.all()
    context={
    'list_teams':list_teams,
        }
    return render(request,"pages/team.html",context)

def blog(request):
    recent_articles=Article.objects.order_by('-updated')[:5]
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

def portfolio(request):
    list_portfolios=Portfolio.objects.all()
    categories=Categorie.objects.all()
    context={
    'list_portfolios':list_portfolios,
    'categories':categories,
        }
    return render(request,"pages/portfolio.html",context)

def detail_portfolio(request,slug:str):
    try:
        portfolio=Portfolio.objects.get(slug=slug)
        context={
            'portfolio':portfolio,
        }
    except Article.DoesNotExist:
        raise('This portfolio doesnot exist')
    return render(request,'pages/detail_portfolio.html',context)

def select_portfolio_categorie(request):
    try:
        portfolio_en_relation=Portfolio.objects.all()
        context={
            'portfolio_en_relation':portfolio_en_relation,
        }
    except Article.DoesNotExist:
        raise('This portfolio doesnot exist')
    return render(request,'pages/select_portfolio_categorie.html',context)
