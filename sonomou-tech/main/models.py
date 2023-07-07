from django.db import models
from django.template.defaultfilters import slugify
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django_quill.fields import QuillField
from django.urls import reverse
from django.utils import timezone
from app_auth.models import *
from  embed_video.fields  import  EmbedVideoField

# Create your models here.
# la class de base 
class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')

    class Meta:
        abstract=True

class ArticleCategorie(BaseModel):
    nom_categorie=models.CharField(max_length=100,verbose_name='Libelle')
    slug=models.SlugField(max_length=200,verbose_name='Slug')

    class Meta:
        verbose_name="Categorie"

    def __str__(self) -> str:
        return self.nom_categorie
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.nom_categorie)
        
        super().save(*args,**kwargs)

class Specialite(BaseModel):
    nom_specialite=models.CharField(name='nom_specialite',verbose_name='Nom_specialite',max_length=200)

    class Meta:
        verbose_name="Specialite"

    def __str__(self) -> str:
        return self.nom_specialite

class Temoignage(BaseModel):
    fullname=models.CharField(max_length=200,name="fullname",verbose_name="Full Name",blank=True,null=True)
    specialite=models.ForeignKey(Specialite,on_delete=models.CASCADE,verbose_name='Specialite',name='specialite',blank=True,null=True)
    photo=models.ImageField(upload_to='temoignage_photo',blank=True,null=True,name="photo",verbose_name='Photo')
    contenu=models.TextField(blank=True,null=True,verbose_name='Contenu',name='contenu')
    status=models.BooleanField(default=False,verbose_name="Status")
    
    class Meta:
        ordering=['-created']
        verbose_name="Temoignage"

    def __str__(self) -> str:
        return self.fullname

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

class Portfolio(BaseModel):
    titre=models.CharField(max_length=100,verbose_name='Titre')
    slug=models.SlugField(blank=True,null=True,max_length=200,verbose_name='Slug')
    date_projet=models.DateField(blank=True,null=True,max_length=100,verbose_name='Date projet')
    url=models.URLField(blank=True,null=True,max_length=100,verbose_name='Url')
    client=models.CharField(blank=True,null=True,max_length=100,verbose_name='Client')
    description=models.TextField(blank=True,null=True,max_length=1000,verbose_name='Description')
    categorie=models.ForeignKey(ArticleCategorie,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_categorie_portfolio',
                                verbose_name='Categorie')
    status=models.BooleanField(default=False,verbose_name="Status")

    class Meta:
        ordering=['-created']
        verbose_name="Portfolio"

    def __str__(self) -> str:
        return self.titre

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.titre)
        
        super().save(*args,**kwargs)

class Slider(BaseModel):
    titre=models.CharField(max_length=200,name="titre",verbose_name="Titre",blank=True,null=True)
    photo=models.ImageField(upload_to='slider',blank=True,null=True,name="photo",verbose_name='Photo')
    contenu=models.TextField(blank=True,null=True,verbose_name='Contenu',name='contenu')
    status=models.BooleanField(default='True',verbose_name='Status')
    
    class Meta:
        ordering=['-created']
        verbose_name="Slider"

    def __str__(self) -> str:
        return self.titre

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

