from django.contrib import admin
from .models import jCategory,jBlogPost

# Register your models here.
admin.site.register(jBlogPost)
admin.site.register(jCategory)