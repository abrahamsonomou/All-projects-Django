from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from e_learning.models import eContact

#serialisation de la classe Contact
class eContactSerializer(ModelSerializer):
    class Meta:
        model=eContact
        fields=['nom','email','sujet','message'] 
