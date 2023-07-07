from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

#serialisation de la classe Teacher
class TeacherSerializer(ModelSerializer):
    photo = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model=Teacher
        fields=['full_name','email','adresse','telephone','qualification','password','description','photo']

#serialisation de la classe Student
class StudentSerializer(ModelSerializer):
    photo = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model=Student
        fields=['full_name','email','adresse','telephone','qualification','password','description','photo','interested_category']        

#serialisation de la classe Student
class CompetenceSerializer(ModelSerializer):
    class Meta:
        model=Competence
        fields=['title','pourcentage','teacher']        

# serialisation de la classe Student
class CourseCategorySerializer(ModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model=CourseCategory
        fields=['title','description','image']   

#serialisation de la classe Cours
class CoursSerializer(ModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model=Cours
        fields=['title','prix','category','teacher','description','image']  
