from django.contrib import admin
from .models import CustomerUser
# Register your models here.

@admin.register(CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin):
    list_display=('username','email','telephone','specialite',)
    ordering=('username',)