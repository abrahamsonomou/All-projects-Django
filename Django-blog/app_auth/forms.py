from django import forms
from django.forms.widgets import TextInput
class LoginForm(forms.Form):
    username=forms.CharField(widget=TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class RegisterForm(forms.Form):
    username=forms.CharField(widget=TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_confirm=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))