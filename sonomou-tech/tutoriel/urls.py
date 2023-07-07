from django.urls import path
from .views import *

urlpatterns = [
    path('',tutoriel,name='tutoriel'),
    path('tutoriel/(?P<pk>[0-9]+)/$',detail_tutoriel,name='detail_tutoriel'),
    path('tutoriel/recherche',search_tutoriel,name='search_tutoriel'),
    
]
