from django.contrib import admin
from .models import *
from  embed_video.admin  import  AdminVideoMixin


# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=('titre','slug','created',)
    list_filter=('titre',)
    prepopulated_fields={'slug':('titre',)}
 
@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    list_display=('titre','lien','lieu','dateEv','created',)
    prepopulated_fields={'slug': ('titre',)}
    ordering=('created',)
    list_filter=('created',)

@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display=('fullname','created',)
    ordering=('fullname',)
    search_field=('fullname',)


# teams
@admin.register(Specialite)
class SpecialiteAdmin(admin.ModelAdmin):
    list_display=('titre',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display=('titre',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=('nom','specialite','grade','created')
    ordering=('nom',)

# Contact
@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display=('created','email',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('nom','email','sujet','created',)
    list_filter=('nom','email',)
    ordering=('nom',)

# Blog
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('titre','auteur','categorie','created')
    list_filter=('titre','auteur',)
    prepopulated_fields={'slug':('titre',)}

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display=('auteur','created','blog',)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display=('titre','created',)
    ordering=('titre',)
    search_field=('titre',)