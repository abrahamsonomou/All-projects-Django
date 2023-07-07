from django import forms
from django.db.models import fields
from django.forms import widgets
from app_web.models import *

class CategorieForm(forms.ModelForm):
    class Meta:
        model=Categorie
        fields=['nom_categorie']
        labels={'nom_categorie':'nom_categorie'}
        widgets={
            'nom_categorie':forms.TextInput(attrs={'class':'form-control'}),
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        # fields=['titre','slug','description1','description2','image','categorie','published']
        fields=['titre','description1','image','categorie','published']
        labels={'titre':'Titre',
                'description1':'Description',
                # 'description2':'Details',
                'categorie':'Categorie',
                'published':'Statut'}
        widgets={
            'titre':forms.TextInput(attrs={'class':'form-control'}),
            'description1':forms.Textarea(attrs={'class':'form-control','rows':15,'cols':'30'}),
            # 'description2':forms.Textarea(attrs={'class':'summernote'}),
            'categorie':forms.Select(attrs={'class':'form-control'}),
            'published':forms.Select(attrs={'class':'form-control'}),
        }
 