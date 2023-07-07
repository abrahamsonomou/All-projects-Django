from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Permis)
admin.site.register(Vehicule)
admin.site.register(Lecon)
admin.site.register(Eleve)
admin.site.register(PaiementEleve)
admin.site.register(Moniteur)
admin.site.register(PaiementMoniteur)
admin.site.register(Cours)
admin.site.register(Galerie)
admin.site.register(Slider)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display=('titre','updated',)
    list_filter=('titre',)

@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display=('nom','updated',)
    ordering=('nom',)
    search_field=('nom',)

    
