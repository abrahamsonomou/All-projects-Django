from django.urls import path
from django.conf import settings
from .views import *

urlpatterns = [
    path('',index,name='index'),
    
    path('profile/details',profile,name='profileDetails'),
    path('profile/<int:pk>',UpdateProfile.as_view(),name='profile'),
    path('mes_cotisations',mes_cotisations,name='mes_cotisations'),
    path('ajout_cotisation',ajout_cotisation,name='ajout_cotisation'),
    
    path('admin/cotisations',les_cotisations,name='les_cotisations'),
    path('admin/cotisations/(?P<pk>[0-9]+)/$',DeleteCotisation.as_view(),name='delete_cotisation'),
    
    path('admin/bureau',le_bureau,name='le_bureau'),
    path('admin/membres',les_membres,name='les_membres'),
    path('admin/bureau/delete/<int:pk>/', deleteMembreBureau, name='bureau_delete'),

    path('admin/reglement',le_reglement,name='le_reglement'),
    path('admin/reglement/delete/<int:pk>/', deleteReglement, name='reglement_delete'),

    path('admin/contact/delete/<int:pk>/', deleteContact, name='contact_delete'),

    path('admin/evenements',les_evenements,name='les_evenements'),
    path('admin/contacts',contacts,name='contacts'),
    path('blog/articles',articles,name='articles'),
    
    path('blog/recherche_article',recherche_articles,name='recherche_articles'),
    path('blog/<slug>/',detail_article,name='detail_article'),
    
    path('reglements',reglements,name='reglements'),
    path('evenements',evenements,name='evenements'),
    path('membres',membres,name='membres'),
    path('membres_bureau',membres_bureau,name='membres_bureau'),
    
    #  path('access_refuse',interdiction,name='access_refuse'),
    path('admin/mes_articles',mes_articles,name='mes_articles'),
    # path('update_article/<slug>/',UpdateArticle.as_view(),name='update_article'),
    # path('delete_article/<slug>/',DeleteArticle.as_view(),name='delete_article'),
    path('admin/ajout_articles',AddArticle.as_view(),name='ajout_articles'),
    # path('mes_articles/<slug>/',detail_article,name='details_article'),
    path('blog/article',blog,name='blog'),
    path('calendrier',calendrier,name='calendrier'),
    path('contact',Contact.as_view(),name='contact'),
    # path('403',handler403,name='403'),

    # contacts
    path(r'api/Contacts/',ContactList.as_view(),name='Contacts/'),
    path(r'api/(?P<pk>[0-9]+)/$', ContactListDetail.as_view(),name='Contactdetails/'),

]
