from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.
class CustomerUser(AbstractUser):
    company=models.CharField(blank=True,null=True,max_length=200,name="company",verbose_name="Company")
    job=models.CharField(blank=True,null=True,max_length=200,name="job",verbose_name="Job")
    contry=CountryField(blank=True,null=True,max_length=200,name="contry",verbose_name="Contry")
    phone=PhoneNumberField(null=True,blank=True,unique=True)
    adresse=models.CharField(blank=True,null=True,max_length=2000,name="adresse",verbose_name="Adresse",unique=True)
    about=models.TextField(blank=True,null=True,name="about",verbose_name="About")
    photo=models.ImageField(upload_to='users',blank=True,null=True,name="photo",verbose_name='Photo')
    twitter=models.URLField(blank=True,null=True,name='twitter',verbose_name="Twitter",max_length=200)
    facebook=models.URLField(blank=True,null=True,name='facebook',verbose_name="Facebook",max_length=200)
    instagram=models.URLField(blank=True,null=True,name='instagram',verbose_name="Instagram",max_length=200)
    linkdin=models.URLField(blank=True,null=True,name='linkdin',verbose_name="Linkdin",max_length=200)
    
    class Meta:
        verbose_name="Profil"

    def __str__(self) -> str:
        return self.username
    
    
