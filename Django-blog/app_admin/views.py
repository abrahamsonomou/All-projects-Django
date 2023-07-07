from distutils.log import log
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

# Create your views here.
@login_required
def dashboard(request):
    list_teams=Team.objects.all()
    context={
    'list_teams':list_teams,
        }
    # if not request.user.is_authenticated:
    #     return redirect('index')
    return render(request,"pages/dashboard.html",context)

@login_required
def profile(request):
    # if not request.user.is_authenticated:
    #     return redirect('index')
    
    return render(request,'pages/profile.html')

@login_required
def mes_articles(request):
    # if not request.user.is_authenticated:
    #     return redirect('index')
    
    # gestion des permissions
    has_perm=False
    if request.user.has_perm("blog.delete_article"):
        has_perm=True
        
    list_article=Article.objects.filter(user=request.user)
    paginator=Paginator(list_article,3)
    page=request.GET.get('page')
    try:
        articles=paginator.page(page)
    except PageNotAnInteger:
        articles=paginator.page(1)
    except EmptyPage:
        articles=paginator.page(paginator.num_pages)
    
    context={
            # 'articles':articles,
            'articles':list_article,
            'page':page,
            'has_perm':has_perm,
            }
    return render(request,'pages/mes_articles.html',context)

@login_required
def ajout_articles(request):
    return render(request,'pages/ajout_articles.html')

class AddArticle(LoginRequiredMixin,CreateView):
    model=Article
    form_class=ArticleForm
    template_name='pages/ajout_articles.html'
    success_url='mes_articles'

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
class UpdateArticle(LoginRequiredMixin,UpdateView):
    model = Article
    form_class=ArticleForm
    template_name = "pages/updateArticle.html"

class DeleteArticle(LoginRequiredMixin,DeleteView):
    model = Article
    success_url='/admin/mes_articles'
    template_confirm="pages/article_confirm_delete.html"

    # gestion des permissions
    def dispatch(self, request, *args,**kwargs):
        if not request.user.has_perm("blog.delete_article"):
            # return redirect('access_refuse')
            raise PermissionDenied
        
        return super().dispatch(request, *args, **kwargs)

@login_required
def detail_article(request,slug:str):
    # if not request.user.is_authenticated:
    #     return redirect('index')
    
    try:
        article=Article.objects.get(slug=slug)
        context={
            'article':article,
        }
    except Article.DoesNotExist:
        raise('This article doesnot exist')
    return render(request,'pages/details_article.html',context)

def interdiction(request):
    return render(request,'pages/interdiction.html')


       