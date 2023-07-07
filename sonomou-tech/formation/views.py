from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser
    
# Create your views here.
def formation(request):
    return render(request,'pages/formation.html')

class TeacherList(generics.ListCreateAPIView):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer
    permission_classes = [IsAdminUser]
    
class TeacherListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer
    permission_classes = [IsAdminUser]

class StudentList(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes = [IsAdminUser]
    
class StudentListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes = [IsAdminUser]
    
class CompetenceList(generics.ListCreateAPIView):
    queryset=Competence.objects.all()
    serializer_class=CompetenceSerializer
    permission_classes = [IsAdminUser]
    
class CompetenceListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Competence.objects.all()
    serializer_class=CompetenceSerializer
    permission_classes = [IsAdminUser]
    
class CourseCategoryList(generics.ListCreateAPIView):
    queryset=CourseCategory.objects.all()
    serializer_class=CourseCategorySerializer
    permission_classes = [IsAdminUser]
    
class CourseCategoryListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=CourseCategory.objects.all()
    serializer_class=CourseCategorySerializer    
    permission_classes = [IsAdminUser]

class CoursList(generics.ListCreateAPIView):
    queryset=Cours.objects.all()
    serializer_class=CoursSerializer
    permission_classes = [IsAdminUser]
    
class CoursListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Cours.objects.all()
    serializer_class=CoursSerializer    
    permission_classes = [IsAdminUser]
