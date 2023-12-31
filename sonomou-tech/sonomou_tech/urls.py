"""sonomou_tech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin-django/', admin.site.urls),
    path('',include('main.urls')),
    path('auth/',include('app_auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# handler403="app_web.views.handler403"
# handler404="app_web.views.handler404"
# handler500="app_web.views.handler500"
# handler503="app_web.views.handler503"