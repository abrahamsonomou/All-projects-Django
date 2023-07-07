from django.urls import path
from .views import *

urlpatterns = [
    path('',dashboard,name='dashboard'),
    path('profile',profile,name='profile'),
    path('access_refuse',interdiction,name='access_refuse'),
    path('mes_articles',mes_articles,name='mes_articles'),
    path('update_article/<slug>/',UpdateArticle.as_view(),name='update_article'),
    path('delete_article/<slug>/',DeleteArticle.as_view(),name='delete_article'),
    path('ajout_articles',AddArticle.as_view(),name='ajout_articles'),
    path('mes_articles/<slug>/',detail_article,name='details_article'),
]
