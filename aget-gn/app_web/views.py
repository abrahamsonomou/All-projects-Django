from urllib import request
from django.shortcuts import redirect, render
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)
from app_web.models import *
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse,HttpResponseRedirect,Http404

from .serializers import *
from rest_framework import  generics
from rest_framework.permissions import IsAdminUser
from django.views.generic.edit import CreateView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponseRedirect

# Create your views here.
# @login_required
def index(request):
    membres_bureau=Bureau.objects.all()
    list_membres=CustomerUser.objects.all()
    list_articles=Article.objects.all()
    list_event=Evenement.objects.all()
 
    context={
    'list_membres':list_membres,
    'membres_bureau':membres_bureau,
    'list_articles':list_articles,
    'list_event':list_event,
        }
    return render(request,"pages/index.html",context)

@login_required
def reglements(request):
    list_reglements=Reglement.objects.all()
    
    context={
    'list_reglements':list_reglements,
        }
    return render(request,"pages/reglements.html",context)

# @login_required
def evenements(request):
    list_evenements=Evenement.objects.order_by('-updated')[:6]
    
    context={
    'list_evenements':list_evenements,
        }
    return render(request,"pages/evenements.html",context)

@login_required
def membres(request):
    list_membres=CustomerUser.objects.all()
    
    context={
    'list_membres':list_membres,
        }
    return render(request,"pages/membres.html",context)

@login_required
def membres_bureau(request):
    membres_bureau=Bureau.objects.all()
    
    context={
    'membres_bureau':membres_bureau,
        }
    return render(request,"pages/membres_bureau.html",context)




@login_required
def les_cotisations(request):
    # gestion des permissions
    # if not request.user.is_staff or not request.user.is_superuser:
    
    if not request.user.is_staff:
        raise PermissionDenied
        # return redirect('403')
    
    has_perm_delete=False
    if request.user.has_perm("aget.delete_cotisation"):
        has_perm_delete=True

    
    has_perm_change=False
    if request.user.has_perm("aget.change_cotisation"):
        has_perm_change=True
    
    form=CotisationForm(request.POST)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        
    les_cotisations=Cotisation.objects.all()
    context={
            'les_cotisations':les_cotisations,
            'has_perm_delete':has_perm_delete,
            'has_perm_change':has_perm_change,
            'form':form,
            }
    return render(request,'pages/les_cotisations.html',context)

class DeleteCotisation(LoginRequiredMixin,DeleteView):
    model = Cotisation
    success_url='admin/cotisations'
    template_confirm="confirm_delete.html"
 
    # gestion des permissions
    def dispatch(self, request, *args,**kwargs):
        if not request.user.has_perm("aget.delete_cotisation"):
            # return redirect('access_refuse')
            raise PermissionDenied
        
        return super().dispatch(request, *args, **kwargs)
    
@login_required
def le_bureau(request):
    # gestion des permissions
    # if not request.user.is_staff or not request.user.is_superuser:
    if not request.user.is_staff:
        raise PermissionDenied
        # return redirect('403')
    
    has_perm_delete=False
    if request.user.has_perm("aget.delete_bureau"):
        has_perm_delete=True

    
    has_perm_change=False
    if request.user.has_perm("aget.change_bureau"):
        has_perm_change=True
        
    form=BureauForm(request.POST)
    le_bureau=Bureau.objects.all()
    context={
            'le_bureau':le_bureau,
            'has_perm_change':has_perm_change,
            'has_perm_delete':has_perm_delete,
            'form':form,
            }

    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()   
        return redirect('le_bureau')

    return render(request,'pages/le_bureau.html',context)

@login_required
def les_membres(request):
    # gestion des permissions
    # if not request.user.is_staff or not request.user.is_superuser:
    if not request.user.is_staff:
        raise PermissionDenied
        # return redirect('403')
    
    has_perm_delete=False
    if request.user.has_perm("aget.delete_customeruser"):
        has_perm_delete=True

    
    has_perm_change=False
    if request.user.has_perm("aget.change_customeruser"):
        has_perm_change=True   
    
    list_membres=CustomerUser.objects.all()
    
    context={
    'list_membres':list_membres,
    'has_perm_delete':has_perm_delete,
    'has_perm_change':has_perm_change,
        }
    return render(request,"pages/les_membres.html",context)

@login_required
def le_reglement(request):
 # gestion des permissions
    # if not request.user.is_staff or not request.user.is_superuser:
    if not request.user.is_staff:
        raise PermissionDenied
        # return redirect('403')
    
    has_perm_delete=False
    if request.user.has_perm("aget.delete_reglement"):
        has_perm_delete=True

    
    has_perm_change=False
    if request.user.has_perm("aget.change_reglement"):
        has_perm_change=True   
        
    form=ReglementForm(request.POST)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save() 
        return redirect('le_reglement')
        
    list_reglements=Reglement.objects.all()
    
    context={
    'list_reglements':list_reglements,
    'has_perm_delete':has_perm_delete,
    'has_perm_change':has_perm_change,
    'form':form,
        }
    return render(request,"pages/le_reglement.html",context)

@login_required
def les_evenements(request):
    
    # gestion des permissions
    # if not request.user.is_staff or not request.user.is_superuser:
    if not request.user.is_staff:
        raise PermissionDenied
        # return redirect('403')
    
    has_perm_delete=False
    if request.user.has_perm("aget.delete_evenement"):
        has_perm_delete=True

    
    has_perm_change=False
    if request.user.has_perm("aget.change_evenement"):
        has_perm_change=True   

    form=EvenementForm(request.POST)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save() 
          
    list_evenements=Evenement.objects.order_by('-updated')
    
    context={
    'list_evenements':list_evenements,
    'has_perm_delete':has_perm_delete,
    'has_perm_change':has_perm_change,
    'form':form,
        }
    return render(request,"pages/les_evenements.html",context)

@login_required
def articles(request):
    # gestion des permissions
    # if not request.user.is_staff or not request.user.is_superuser:
    if not request.user.is_staff:
        raise PermissionDenied
        
        # return redirect('403')
    
    has_perm=False
    if request.user.has_perm("aget.delete_article"):
        has_perm=True

    list_articles=Article.objects.order_by('-updated')
    categories=Categorie.objects.all()
    
    paginator=Paginator(list_articles,6)
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
            'categories':categories,
            'has_perm':has_perm,
            }
    return render(request,'pages/articles.html',context)

@login_required
def recherche_articles(request):
    # gestion des permissions
    # if not request.user.is_staff or not request.user.is_superuser:
    if not request.user.is_staff:
        raise PermissionDenied
        
        # return redirect('403')
    
    has_perm=False
    if request.user.has_perm("aget.delete_article"):
        has_perm=True
        
    query=request.GET["article"]
    list_articles=Article.objects.filter(titre__icontains=query)
    
    categories=Categorie.objects.all()
    
    paginator=Paginator(list_articles,6)
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
            'categories':categories,
            'has_perm':has_perm,
            }
    return render(request,'pages/recherche_articles.html',context)

def detail_article(request,slug:str):
    try:
        article=Article.objects.get(slug=slug)
        context={
            'article':article,
        }
    except Article.DoesNotExist:
        raise('This article doesnot exist')
    return render(request,'pages/detail_article.html',context)
        
@login_required
def mes_articles(request):
    # gestion des permissions
    # if not request.user.is_staff or not request.user.is_superuser:
    if not request.user.is_auteur:
        # return redirect('403')
        raise PermissionDenied

    has_perm_delete=False
    if request.user.has_perm("aget.delete_article"):
        has_perm_delete=True

    
    has_perm_change=False
    if request.user.has_perm("aget.change_article"):
        has_perm_change=True
    
            
    list_article=Article.objects.filter(user=request.user)
    context={
            'articles':list_article,
            'has_perm_delete':has_perm_delete,
            'has_perm_change':has_perm_change,
            }
    return render(request,'pages/mes_articles.html',context)


class AddArticle(LoginRequiredMixin,CreateView):
    model=Article
    form_class=ArticleForm
    template_name='pages/ajout_articles.html'
    success_url='mes_articles'

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
    def dispatch(self, request, *args,**kwargs):
        # if not request.user.has_perm("blog.add_article"):
        if not request.user.is_auteur:
            # return redirect('403')
            raise PermissionDenied
        
        return super().dispatch(request, *args, **kwargs)

    
# @login_required
def blog(request):
    
    # gestion des permissions
    has_perm=False
    if request.user.has_perm("aget.delete_article"):
        has_perm=True
        
    list_articles=Article.objects.order_by('-updated')
    
    paginator=Paginator(list_articles,3)
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
            'has_perm':has_perm,
            }
    return render(request,'pages/posts.html',context)

# @login_required
def contacts(request):
    # gestion des permissions
    # if not request.user.is_staff or not request.user.is_superuser:
    if not request.user.is_staff:
        # return redirect('403')
        raise PermissionDenied

    has_perm_delete=False
    if request.user.has_perm("aget.delete_contacts"):
        has_perm_delete=True
    
    contacts=Contacts.objects.order_by('-updated')
    
    context={
    'contacts':contacts,
    'has_perm_delete':has_perm_delete,
    
        }
    return render(request,"pages/contacts.html",context)

class Contact(CreateView):
    model=Contacts
    form_class=ContactForm
    template_name='pages/contact.html'
    success_url='blog/article'

# @login_required
def calendrier(request):
    return render(request,'pages/calendrier.html')

@login_required
def ajout_cotisation(request):
    form=CotisationForm(request.POST)
    # print(333333333333387)
    if True:
        # print(333333333333333333333)
        motif=request.POST.get('motif')
        montant=request.POST.get('montant')
        mode_payement=request.POST.get('mode_payement')
        telephone=request.POST.get('telephone')

        import http.client
        import json

        conn = http.client.HTTPSConnection('paygateglobal.com')

        headers = {'Content-type': 'application/json'}

        foo = {
                            "auth_token" : "c038a374-b987-475a-abf9-5895f3a56b1b",
                            "amount" : montant,
                            "description" : motif,
                            "identifier" : '202206180014444',
                            "phone_number" : telephone,
                            "network" : mode_payement
        }

        json_data = json.dumps(foo)

        conn.request('POST', '/api/v1/pay/', json_data, headers)

        response = conn.getresponse()
        print(response.read().decode())
        # form.instance.membre=request.user
        #instance=form.save(commit=False)
        #instance.save()  
                #  

         
    context={
            'form':form,
            }
    return render(request,'pages/ajout_cotisation.html',context)

# Membre

@login_required
def profile(request):
    # if not request.user.is_authenticated:
    #     return redirect('index')
    return render(request,'pages/profile.html')

@login_required
def mes_cotisations(request):
    # if not request.user.is_authenticated:
    #     return redirect('index')
    
    # gestion des permissions
    has_perm=False
    if request.user.has_perm("aget.delete_cotisation"):
        has_perm=True
        
    mes_cotisations=Cotisation.objects.filter(membre=request.user)
    context={
            'mes_cotisations':mes_cotisations,
            'has_perm':has_perm,
            }
    return render(request,'pages/mes_cotisations.html',context)

class UpdateProfile(LoginRequiredMixin,UpdateView):
    model = CustomerUser
    form_class=ProfileForm
    template_name = "pages/profile.html"
    # success_url='/blog'
    # redirect_field_name='/blog'
    success_url='http://127.0.0.1:8000/blog/article'

# les methodes de la classe Contacts    
class ContactList(generics.ListCreateAPIView):
    queryset=Contacts.objects.all()
    serializer_class=ContactSerializer
    permission_classes = [IsAdminUser]
    
class ContactListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Contacts.objects.all()
    serializer_class=ContactSerializer    
    permission_classes = [IsAdminUser]

# suppression
@login_required
def deleteReglement(request, pk):
	reglement = Reglement.objects.get(id=pk)

	if request.user.has_perm("aget.delete_reglement"):
		reglement.delete()
	else:
		raise Http404
	
	return redirect('le_reglement')

@login_required
def deleteMembreBureau(request, pk):
	reglement = Bureau.objects.get(id=pk)

	if request.user.has_perm("aget.delete_bureau"):
		reglement.delete()
	else:
		raise Http404
	
	return redirect('le_bureau')

@login_required
def deleteContact(request, pk):
	reglement = Contacts.objects.get(id=pk)
    
	if request.user.has_perm("aget.delete_contact"):
		reglement.delete()
	else:
		raise Http404
	
	return redirect('contacts')

# gestion des erreurs
def handler403(request,exception):
    return render(request,'pages/403.html')

def handler404(request, exception):
    return render(request,'pages/404.html',status=404)

def handler500(request):
    return render(request,'pages/500.html')

def handler503(request,exception):
    return render(request,'pages/503.html')    

