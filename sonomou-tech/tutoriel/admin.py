from .models import *
from  embed_video.admin  import  AdminVideoMixin
from django.contrib import admin

# Register your models here.
@admin.register(Tutoriel)
class TutorielAdmin(AdminVideoMixin,admin.ModelAdmin):
    list_display=('titre','slug','image','auteur','categorie','created',)
    list_filter=('titre','auteur',)
    prepopulated_fields={'slug':('titre',)}
    