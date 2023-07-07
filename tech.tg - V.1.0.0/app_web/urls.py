from django.urls import path
from django.conf import settings
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('/about',about,name='about'),

    path('/blog',blog,name='blog'),
    path('blog/<slug>/',detail_article,name='detail_article'),
    path('article/recherche',search_article,name='search_article'),

    # path('/book',book,name='book'),
    # path('book/<slug>/',detail_book,name='detail_book'),
    # path('book/recherche',search_book,name='search_book'),

    path('/tutoriel',tutoriel,name='tutoriel'),
    path('tutoriel/<slug>/',detail_tutoriel,name='detail_tutoriel'),
    path('tutoriel/recherche',search_tutoriel,name='search_tutoriel'),
    
    path('/formations',formations,name='formations'),
    path('formations/<slug>/',detail_formations,name='detail_formations'),
    path('formations/recherche',search_formations,name='search_formations'),

    path('/team',team,name='team'),

    path('contact',Contact.as_view(),name='contact'),
    
    path('newletter',newletter,name='newletter'),
    
    # path('newletter',NewLetter.as_view(),name='newletter'),
]
