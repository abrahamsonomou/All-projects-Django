from django.db import models
from django.urls import reverse
import uuid
from parametres.models import Profession

class FAQ(models.Model):
    titre=models.CharField(max_length=200,verbose_name="Titre")
    description=models.TextField(blank=True,null=True,name="description",verbose_name="Description")
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
    
    def __str__(self) -> str:
        return self.titre

class Galerie(models.Model):
    titre=models.CharField(max_length=200,name="titre",verbose_name="Titre",blank=True,null=True)
    photo=models.ImageField(upload_to='galerie',blank=True,null=True,name="photo",verbose_name='Photo')
    statut=models.BooleanField(default='True',verbose_name='Status')
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    
    class Meta:
        ordering=['-updated']
        verbose_name="Galerie"

    def __str__(self) -> str:
        return self.titre

class Departement(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    nom_departement=models.CharField(max_length=100,verbose_name='nom_departement')
    # description=QuillField(blank=True,null=True,max_length=200,verbose_name='Description')
    image=models.ImageField(upload_to='Departements_images',blank=True,null=True,name="image",verbose_name='Image')
    statut=models.BooleanField(default=False,verbose_name="Statut")
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    
    class Meta:
        ordering=['-updated']
        verbose_name="Departement"

    def __str__(self) -> str:
        return self.nom_departement

# Contact
class Contact(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    nom=models.CharField(blank=True,null=True,max_length=100,name='nom',verbose_name='Nom')
    email=models.EmailField(blank=True,null=True,max_length=100,name='email',verbose_name='Email')
    sujet=models.CharField(blank=True,null=True,max_length=100,name='sujet',verbose_name='Sujet')
    message=models.TextField(blank=True,null=True,verbose_name='Message',name='message')
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    
    class Meta:
        ordering=['-updated']
        verbose_name="Contact" 

    def __str__(self) -> str:
        return self.nom

class NewsLetter(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email=models.EmailField(blank=True,null=True,max_length=100,verbose_name='Email',name='email')
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    
    class Meta:
        verbose_name="NewsLetter"
        ordering=['-updated']

    def __str__(self) -> str:
        return self.email

class Temoignage(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    nom=models.CharField(max_length=200)
    contenu=models.TextField(blank=True,null=True)
    photo=models.ImageField(upload_to='Temoignage',blank=True,null=True,verbose_name='Poster')
    profession=models.ForeignKey(Profession,on_delete=models.SET_NULL, blank=True,null=True,)
    statut=models.BooleanField(default=False,verbose_name="Statut")
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Temoignage'
        verbose_name_plural = 'Temoignages'
    
    def __str__(self) -> str:
        return self.nom

class Service(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    titre=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True,verbose_name="Description")
    classe=models.CharField(max_length=200)
    image=models.ImageField(upload_to='services',blank=True,null=True,verbose_name='Poster')
    statut=models.BooleanField(default=False,verbose_name="Statut")
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    
    def __str__(self) -> str:
        return self.titre