from django.contrib import admin
from .models import (
    eCategory,eSubCategory, eBlogPost,
    eContact, eNewsLetter
)
from import_export.admin import ImportExportModelAdmin
from parler.admin import TranslatableAdmin

# Register your models here.
class eCategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=['category_name','active',]
admin.site.register(eCategory,TranslatableAdmin)
# admin.site.register(eCategory,eCategoryAdmin)

class eSubCategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=['sub_category_name','category','active',]
admin.site.register(eSubCategory,eSubCategoryAdmin)

class eBlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=['title','author', 'category', 'tags', 'views', 'is_popular', 'created_on', 'updated_on', 'status',]

admin.site.register(eBlogPost,eBlogAdmin)

# contact
class ContactAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('nom','email','message','updated')
admin.site.register(eContact,ContactAdmin)


class NewsLetterAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('email','created',)
admin.site.register(eNewsLetter,NewsLetterAdmin)

# End contact