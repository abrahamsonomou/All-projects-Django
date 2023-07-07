from django.contrib import admin
from .models import *

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display=('titre','updated',)
    list_filter=('titre',)

admin.site.register(Galerie)

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display=('nom_departement','created',)
    list_filter=('nom_departement',)

admin.site.register(Contact)

@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display=('created','email',)
   
   
@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display=('nom','updated',)
    ordering=('nom',)
    search_field=('nom',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=('titre','created',)
    list_filter=('titre',)

