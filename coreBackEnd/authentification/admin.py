from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from authentification.models import User,Student,Teacher

# Register your models here.
@admin.register(User)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display =('username', 'email', 'session_token', 'created_at', 'updated_at', 'is_active', )
    ordering=('updated_at',)  

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('user','interested_category',)

@admin.register(Teacher)
class TeacherAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('user',)

    