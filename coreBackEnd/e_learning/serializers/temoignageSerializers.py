from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from e_learning.models import eLearningTemoignage

    # Temoignage       
class TemoignageSerializer(ModelSerializer):
    photo = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model=eLearningTemoignage
        fields=['nom','contenu','photo'] 
        