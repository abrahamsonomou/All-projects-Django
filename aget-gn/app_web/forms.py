from django import forms
from django.db.models import fields
from django.forms import widgets
from app_web.models import *
from app_auth.models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contacts
        fields=['nom','email','message']
        labels={'nom':'Full Name','email':'Email ','message':'Message'}
        widgets={
            'nom':forms.TextInput(attrs={'class':'form-control','placeholder':"Enter your full name",'required':'required',}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':"Enter your email",'required':'required',}),
            'message':forms.Textarea(attrs={'class':'form-control','cols':30,'rows':10,'placeholder':"Enter your message",'required':'required',})
        }

# class CategorieForm(forms.ModelForm):
#     class Meta:
#         model=Categorie
#         fields=['nom_categorie']
#         labels={'nom_categorie':'nom_categorie'}
#         widgets={
#             'nom_categorie':forms.TextInput(attrs={'class':'form-control'}),
#         }

class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=['titre','description','image','categorie','statut']
        labels={'titre':'Titre',
                'description':'Description',
                'categorie':'Categorie',
                'statut':'Statut'}
        widgets={
            'titre':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':15,'cols':'30'}),
            'categorie':forms.Select(attrs={'class':'form-control'}),
            'statut':forms.CheckboxInput(attrs={'class':'form-control'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model=CustomerUser
        fields=['first_name','last_name','email','telephone','ecole','annee','formation','specialite','adresse',
                'date_naissance','facebook','instagram','linkdin','twitter','detail','photo']
        labels={'first_name':'first_name',
                'last_name':'last_name',
                'telephone':'telephone',
                'ecole':'ecole',
                'annee':'annee',
                'formation':'formation',
                'specialite':'specialite',
                'adresse':'adresse',
                'date_naissance':'date_naissance',
                'facebook':'facebook',
                'instagram':'instagram',
                'linkdin':'linkdin',
                'twitter':'twitter',
                'detail':'detail',
                'photo':'photo',
                'email':'email',
                }
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'telephone':forms.TextInput(attrs={'class':'form-control'}),
            'ecole':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'annee':forms.DateInput(attrs={'class':'form-control'}),
            'formation':forms.TextInput(attrs={'class':'form-control'}),
            'specialite':forms.TextInput(attrs={'class':'form-control'}),
            'adresse':forms.TextInput(attrs={'class':'form-control'}),
            'date_naissance':forms.TextInput(attrs={'class':'form-control'}),
            'facebook':forms.TextInput(attrs={'class':'form-control'}),
            'instagram':forms.TextInput(attrs={'class':'form-control'}),
            'linkdin':forms.TextInput(attrs={'class':'form-control'}),
            'twitter':forms.TextInput(attrs={'class':'form-control'}),
            'detail':forms.Textarea(attrs={'class':'form-control'}),
            # 'photo':forms.TextInput(attrs={'class':'form-control'}),
        }

class CotisationForm(forms.ModelForm):
    class Meta:
        model=Cotisation
        fields=['motif','telephone','montant',]
        labels={'motif':'Motif','telephone':'telephone ','montant':'montant',}
        widgets={
            'motif':forms.TextInput(attrs={'class':'form-control','placeholder':"motif",'required':'required',}),
            'telephone':forms.TextInput(attrs={'class':'form-control','required':'required',}),
            'montant':forms.NumberInput(attrs={'class':'form-control','required':'required',}),
            #'mode_payement':forms.Select(attrs={'class':'form-control','required':'required',})
        }

class BureauForm(forms.ModelForm):
    class Meta:
        model=Bureau
        fields=['fonction','membre','memdat',]
        widgets={
            'fonction':forms.TextInput(attrs={'class':'form-control','required':'required',}),
            'membre':forms.Select(attrs={'class':'form-control','required':'required',}),
            'memdat':forms.TextInput(attrs={'class':'form-control','required':'required',}),
        }
        
class ReglementForm(forms.ModelForm):
    class Meta:
        model=Reglement
        fields=['titre_reglement','description',]
        widgets={
            'titre_reglement':forms.TextInput(attrs={'class':'form-control','required':'required',}),
            'description':forms.Textarea(attrs={'class':'form-control','required':'required',}),
        }

class EvenementForm(forms.ModelForm):
    class Meta:
        model=Evenement
        fields=['titre_event','description','image','lieu','dateEv','lien','heure']
        widgets={
            'titre_event':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':15,'cols':'30'}),
            'lieu':forms.TextInput(attrs={'class':'form-control'}),
            'dateEv':forms.TextInput(attrs={'class':'form-control datepicker'}),
            'lien':forms.TextInput(attrs={'class':'form-control'}),
            'heure':forms.TextInput(attrs={'class':'form-control timepicker'}),
        }
        