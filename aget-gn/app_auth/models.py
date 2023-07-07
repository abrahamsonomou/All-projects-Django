from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
import uuid

# Create your models here.

class UserProfileManager(BaseUserManager):
    def create_user(self,email,username,password=None,*callback_args, **callback_kwargs):
        
        if not email:
            raise ValueError('Desolé, veuillez saisir un email')
        
        email=self.normalize_email(email)
        user=self.model(email=email,username=username)
        
        user.set_password(password)
        
        # user=self.model(username=username,password=password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password):
        user=self.create_user(email,username,password)
        
        user.is_staff=True
        user.is_active=True
        user.is_auteur=True
        user.is_superuser=True
        
        user.save(using=self._db)
        return user   
    
class CustomerUser(AbstractUser):
    # uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    telephone=PhoneNumberField(null=True,blank=True)
    adresse=models.CharField(blank=True,null=True,max_length=2000,name="adresse",verbose_name="Adresse")
    annee=models.CharField(blank=True,null=True,max_length=2000,verbose_name="Annee")
    formation=models.CharField(blank=True,null=True,max_length=2000,verbose_name="Formation")
    detail=models.TextField(blank=True,null=True,verbose_name="Detail")
    ecole=models.CharField(max_length=2000,blank=True,null=True,verbose_name="Université")
    date_naissance=models.DateField(blank=True,null=True,verbose_name="Date naissance")
    photo=models.ImageField(upload_to='users_avatar',blank=True,null=True,name="photo",verbose_name='Photo')
    specialite=models.CharField(blank=True,null=True,name="specialite",verbose_name="specialite",max_length=200,)
    twitter=models.CharField(blank=True,null=True,name='twitter',verbose_name="Twitter",max_length=200)
    facebook=models.CharField(blank=True,null=True,name='facebook',verbose_name="Facebook",max_length=200)
    instagram=models.CharField(blank=True,null=True,name='instagram',verbose_name="Instagram",max_length=200)
    linkdin=models.CharField(blank=True,null=True,name='linkdin',verbose_name="Linkdin",max_length=200)
    email=models.EmailField(blank=True,null=True,verbose_name="Email",max_length=200,unique=True)
    last_name=models.CharField(blank=True,null=True,verbose_name="name",max_length=200,unique=True)
    first_name=models.CharField(max_length=2000,blank=True,null=True)
    username=models.CharField(max_length=2000,blank=True,null=True,unique=True)
    is_auteur=models.BooleanField(default=False,blank=True,null=True)
    is_active=models.BooleanField(default=False,blank=True,null=True)
    is_membre=models.BooleanField(default=False,blank=True,null=True)
    
    USERNAME_FIELD='username'
    # REQUIRED_FIELDS=['username']
    
    objects= UserProfileManager()
    
    class Meta:
        verbose_name="Profil"

    def __str__(self) -> str:
        return self.username
    

