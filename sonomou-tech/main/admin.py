from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ArticleCategorie)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display=('nom_categorie',)
    list_filter=('nom_categorie',)
    prepopulated_fields={'slug':('nom_categorie',)}


@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display=('fullname','created',)
    ordering=('fullname',)
    search_field=('fullname',)

@admin.register(Specialite)
class SpecialiteAdmin(admin.ModelAdmin):
    list_display=('nom_specialite',)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display=('titre','slug','created',)
    list_filter=('titre',)
    prepopulated_fields={'slug':('titre',)}

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display=('titre','created',)
    ordering=('titre',)
    search_field=('titre',)
    