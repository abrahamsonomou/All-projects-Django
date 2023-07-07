from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(CourseCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','created',)
    prepopulated_fields={'slug':('title',)}
    
class CompetenceAdmin(admin.StackedInline):
    model= Competence

class TeacherAdmin(admin.ModelAdmin):
    inlines=[CompetenceAdmin]


admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Competence)
admin.site.register(Student)
admin.site.register(Cours)