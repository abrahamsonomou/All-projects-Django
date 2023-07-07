from django.contrib import admin
from .models import *
from  embed_video.admin  import  AdminVideoMixin


# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=('titre','slug','created',)
    list_filter=('titre',)
    prepopulated_fields={'slug':('titre',)}

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display=('titre','slug','created',)
    list_filter=('titre',)
    prepopulated_fields={'slug':('titre',)}
    
@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display=('fullname','created',)
    ordering=('fullname',)
    search_field=('fullname',)

# teams
@admin.register(Specialite)
class SpecialiteAdmin(admin.ModelAdmin):
    list_display=('nom_specialite',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display=('nom_grade',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=('nom','specialite','grade','created')
    ordering=('nom',)

# Contact
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('nom','email','sujet','message','created',)
    list_filter=('nom','email',)
    ordering=('nom',)

# Blog

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display=('nom_categorie',)

@admin.register(BlogTags)
class BlogTagsAdmin(admin.ModelAdmin):
    list_display=('title',)
        
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('titre','user','categorie','created')
    list_filter=('titre','user',)
    prepopulated_fields={'slug':('titre',)}

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display=('user','created','blog',)
