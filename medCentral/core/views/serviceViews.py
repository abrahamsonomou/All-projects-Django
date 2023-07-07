from django.shortcuts import render
from rest_framework.views import APIView
from  core.models import Service
from core.serializers.serviceSerializers import ServiceSerializer
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser
from django.http import HttpResponse,HttpResponseRedirect,Http404

def services(request):
    services=Service.objects.filter(statut=True)
    context={
        'services':services,
        }
    return render(request,"services/services.html",context)

# services 
class ServiceList(generics.ListCreateAPIView):
    queryset=Service.objects.all().order_by('-updated')
    serializer_class=ServiceSerializer
    
class ServiceListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Service.objects.all()
    serializer_class=ServiceSerializer 