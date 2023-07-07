from django.shortcuts import render
from rest_framework.views import APIView
from  e_learning.serializers import temoignageSerializers
from e_learning.models import eLearningTemoignage
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser
from django.http import HttpResponse,HttpResponseRedirect,Http404

def temoignage(request):
    return render(request,"pages/temoignage.html")

# rest_framwork
# Temoignage       
class TemoignageList(generics.ListCreateAPIView):
    queryset=eLearningTemoignage.objects.all().order_by('-updated')
    serializer_class=temoignageSerializers
    
class TemoignageListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=eLearningTemoignage.objects.all()
    serializer_class=temoignageSerializers  
  