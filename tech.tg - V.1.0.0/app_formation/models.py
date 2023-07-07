from distutils.command.upload import upload
from django.contrib.auth import get_user_model
from django_quill.fields import QuillField
from django.template.defaultfilters import slugify
from  embed_video.fields  import  EmbedVideoField
from django.utils import timezone
from django.db import models

# Create your models here.
User=get_user_model()

class Category(models.Model):
    titre=models.CharField(max_length=100,verbose_name='Libelle')

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categorys'
    
    def __str__(self) -> str:
        return self.titre

class Niveau(models.Model):
    titre=models.CharField(verbose_name='niveau',max_length=200)
    class Meta:
        verbose_name='Niveau'
        verbose_name_plural='Niveaux'
    
    def __str__(self) -> str:
        return self.titre

class Formation(models.Model):
    titre=models.CharField(max_length=100,verbose_name='Titre')
    slug=models.SlugField(max_length=200,verbose_name='Slug',blank=True,null=True)
    description1=models.TextField(blank=True,null=True,name="description1",verbose_name="Description1")
    description2=QuillField(blank=True,null=True,name="description2",verbose_name="Description2")
    image=models.ImageField(upload_to='formations',blank=True,null=True,name="image",verbose_name='Image')
    niveau=models.ForeignKey(Niveau,on_delete=models.SET_NULL,blank=True,null=True,max_length=200,verbose_name='niveau')
    plublish=models.DateTimeField(default=timezone.now())
    published=models.BooleanField(default=False,verbose_name="Publie")
    auteur=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_user',
                                verbose_name='Auteur')
    categorie=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_category',
                                verbose_name='Category')
    created=models.DateTimeField(auto_now = False, auto_now_add = True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')


    class Meta:
        verbose_name="Formation"

    def __str__(self) -> str:
        return self.titre

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.titre)
        
        super().save(*args,**kwargs)

class Cours(models.Model):
    titre=models.CharField(max_length=100,verbose_name='Titre')
    slug=models.SlugField(max_length=200,blank=True,null=True,verbose_name='Slug')
    description=QuillField(blank=True,null=True,name="description",verbose_name="Description")
    image=models.ImageField(upload_to='formations',blank=True,null=True,name="image",verbose_name='Image')
    formation=models.ForeignKey(Formation,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_formations',
                                verbose_name='Formations')
    video=EmbedVideoField(blank=True,null=True)
    plublish=models.DateTimeField(default=timezone.now())
    published=models.BooleanField(default=False,verbose_name="Publie")
    created=models.DateTimeField(auto_now_add=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')

    class Meta:
        verbose_name="Cour"

    def __str__(self) -> str:
        return self.titre

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.titre)
        
        super().save(*args,**kwargs)

class Tutoriel(models.Model):
    titre=models.CharField(max_length=100,verbose_name='Titre')
    slug=models.SlugField(max_length=200,verbose_name='Slug',blank=True,null=True)
    description=models.TextField(blank=True,null=True,name="description",verbose_name="Description")
    image=models.ImageField(upload_to='tutoriels',blank=True,null=True,name="image",verbose_name='Poster')
    auteur=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_user_tuto',
                                verbose_name='Auteur')
    categorie=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_category_tuto',
                                verbose_name='Category')
    url=EmbedVideoField(blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    published=models.BooleanField(default=False,verbose_name="Publie")
    plublish=models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name="Tutoriel"
        ordering=['-created']


    def __str__(self) -> str:
        return self.titre
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.titre)
        
        super().save(*args,**kwargs)
