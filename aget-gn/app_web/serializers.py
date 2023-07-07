from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

#serialisation de la classe Contact
class ContactSerializer(ModelSerializer):
    class Meta:
        model=Contacts
        fields=['nom','email','message'] 

#serialisation de la classe Categorie
class CategorieSerializer(ModelSerializer):
    class Meta:
        model=Categorie
        fields=['nom_categorie',] 

#serialisation de la classe Evenement
class EvenementSerializer(ModelSerializer):
    class Meta:
        model=Evenement
        fields=['titre_event','description','image','lien','lieu','heure','dateEv'] 

#serialisation de la classe reglement
class ReglementSerializer(ModelSerializer):
    class Meta:
        model=Reglement
        fields=['titre','description'] 

#serialisation de la classe Bureau
class BureauSerializer(ModelSerializer):
    class Meta:
        model=Bureau
        fields=['fonction','memdat','membre'] 

#serialisation de la classe Cotisation
class CotisationSerializer(ModelSerializer):
    class Meta:
        model=Cotisation
        fields=['motif','membre','montant','mode_payement'] 

#serialisation de la classe Article
class ArticleSerializer(ModelSerializer):
    class Meta:
        model=Article
        fields=['titre','description','user','categorie','image','statut']

#serialisation de la classe Commentaire
class CommentaireSerializer(ModelSerializer):
    class Meta:
        model=Commentaire
        fields=['article','user','content']




