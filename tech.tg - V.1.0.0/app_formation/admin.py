from django.contrib import admin
from .models import *
from  embed_video.admin  import  AdminVideoMixin

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('titre',)
    ordering=('titre',)

@admin.register(Niveau)
class NiveauAdmin(admin.ModelAdmin):
    list_display=('titre',)
    ordering=('titre',)

@admin.register(Tutoriel)
class TutorielAdmin(AdminVideoMixin,admin.ModelAdmin):
    list_display=('titre','slug','image','auteur','categorie','created',)
    list_filter=('titre','auteur',)
    prepopulated_fields={'slug':('titre',)}

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display=('titre','created','auteur')
    prepopulated_fields={'slug': ('titre',)}
    search_fields=('titre','categorie')
    ordering=('auteur',)
    list_filter=('auteur','created',"titre","niveau",)

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display=('titre','created',)
    prepopulated_fields={'slug': ('titre',)}
    search_fields=('titre',)
    ordering=('titre',)
    list_filter=('created',"titre",)

