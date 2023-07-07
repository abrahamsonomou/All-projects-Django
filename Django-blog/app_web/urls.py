from django.urls import path
from django.conf import settings
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('about',about,name='about'),
    path('service',service,name='service'),
    # path('contact',contact,name='contact'),
    path('contact',Contact.as_view(),name='contact'),

    path('blog',blog,name='blog'),
    path('blog/<slug>/',detail_article,name='detail_article'),
    path('article/recherche',search_article,name='search_article'),

    path('team',team,name='team'),
    
    path('portfolio',portfolio,name='portfolio'),
    path('portfolio/<slug>/',detail_portfolio,name='detail_portfolio'),
    path('portfolio/<categorie>/',select_portfolio_categorie,name='select_portfolio_categorie'),
    
]
