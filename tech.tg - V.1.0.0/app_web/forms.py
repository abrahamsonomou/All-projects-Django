from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Contact,NewsLetter

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['nom','email','message','sujet']
        labels={'nom':'Full Name','email':'Email Address','message':'Message','sujet':'Sujet'}
        widgets={
            'nom':forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':"Enter your full name"}),
            'email':forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':"Enter your email"}),
            'sujet':forms.TextInput(attrs={'class':'rounded form-control mr-2 py-3','placeholder':"Enter your sujet"}),
            'message':forms.Textarea(attrs={'class':'form-control','cols':30,'rows':10,'placeholder':"Enter your message"})
        }
class NewLetterForm(forms.ModelForm):
    class Meta:
        model=NewsLetter
        fields=['email']
        widgets={
                'email':forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':"Enter your email"}),
            }
        def clean_field(self):
            email = self.cleaned_data.get('email')
            
            return email
        
