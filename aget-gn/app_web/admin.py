from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    list_display=('titre_event','created',)
    list_filter=('titre_event',)
    prepopulated_fields={'slug':('titre_event',)}

@admin.register(Reglement)
class ReglementAdmin(admin.ModelAdmin):
    list_display=('titre_reglement','created',)
    list_filter=('titre_reglement',)
    prepopulated_fields={'slug':('titre_reglement',)}
    
@admin.register(Bureau)
class BureauAdmin(admin.ModelAdmin):
    list_display=('membre','fonction','memdat','created',)
    list_filter=('fonction','memdat',)

@admin.register(Cotisation)
class CotisationAdmin(admin.ModelAdmin):
    list_display=('membre','motif','montant','mode_payement','created',)
    list_filter=('motif','montant',)

@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display=('nom','email','message',)
    
# blog
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display=('nom_categorie',)
    prepopulated_fields={'slug':('nom_categorie',)}
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('titre','user','categorie','created')
    list_filter=('titre','user',)
    prepopulated_fields={'slug':('titre',)}

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display=('user','created','article',)
    
    