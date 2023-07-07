from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django_quill.fields import QuillField

# Create your models here.
CHOIX_GRADE={
    ('licence','Licence'),
    ('master','Master'),
    ('doctorat','Doctorat'),
    ('bts','BTS'),
    ('autre','Autre'),
}    
class CustomerUser(AbstractUser):
    phone=PhoneNumberField(null=True,blank=True,unique=True)
    contry=CountryField(blank=True,null=True,max_length=200,name="contry",verbose_name="Contry")
    adresse=models.CharField(blank=True,null=True,max_length=2000,name="adresse",verbose_name="Adresse",unique=True)
    about=models.TextField(blank=True,null=True,name="about",verbose_name="About")
    description=QuillField(blank=True,null=True,max_length=200,verbose_name='Description')
    photo=models.ImageField(upload_to='users_avatar',blank=True,null=True,name="photo",verbose_name='Photo')
    specialite=models.CharField(blank=True,null=True,name="specialite",verbose_name="specialite",max_length=200,)
    grade=models.TextField(blank=True,null=True,name="grade",verbose_name="Grade",choices=CHOIX_GRADE)
    twitter=models.URLField(blank=True,null=True,name='twitter',verbose_name="Twitter",max_length=200)
    facebook=models.URLField(blank=True,null=True,name='facebook',verbose_name="Facebook",max_length=200)
    instagram=models.URLField(blank=True,null=True,name='instagram',verbose_name="Instagram",max_length=200)
    linkdin=models.URLField(blank=True,null=True,name='linkdin',verbose_name="Linkdin",max_length=200)
    is_staff=models.BooleanField(default=False,blank=True,null=True)
    class Meta:
        verbose_name="Profil"

    def __str__(self) -> str:
        return self.username
    
    
