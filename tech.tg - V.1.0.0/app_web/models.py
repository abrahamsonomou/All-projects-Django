
# Create your models here.
from django_quill.fields import QuillField
from  embed_video.fields  import  EmbedVideoField
from django.template.defaultfilters import slugify
from phonenumber_field.modelfields import PhoneNumberField
from app_auth.models import *
from app_formation.models import *
from django.db import models


# Create your models here.

# teams
class Specialite(models.Model):
    titre=models.CharField(name='titre',verbose_name='Titre',max_length=200)

    class Meta:
        verbose_name="Specialite"

    def __str__(self) -> str:
        return self.titre


class Grade(models.Model):
    titre=models.CharField(name='titre',verbose_name='Titre',max_length=200)

    class Meta:
        verbose_name="Grade"

    def __str__(self) -> str:
        return self.titre


class Evenement(models.Model):
    titre=models.CharField(max_length=100,verbose_name='Titre')
    slug=models.SlugField(max_length=200,verbose_name='Slug',blank=True,null=True)
    description=QuillField(blank=True,null=True,name="description",verbose_name="Description")
    poster=models.ImageField(upload_to='events_images',blank=True,null=True,name="poster",verbose_name='Poster')
    url=EmbedVideoField(blank=True,null=True)
    lien=models.URLField(blank=True,null=True,verbose_name='Lien')
    lieu=models.CharField(max_length=100,verbose_name='Lieu')
    dateEv=models.DateField(auto_now_add=True,verbose_name='Date')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')

    class Meta:
        verbose_name="Evenement"
        ordering=['-created']


    def __str__(self) -> str:
        return self.titre
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.titre)
        
        super().save(*args,**kwargs)

class Service(models.Model):
    titre=models.CharField(max_length=100,verbose_name='Titre')
    slug=models.SlugField(blank=True,null=True,max_length=200,verbose_name='Slug')
    description=models.TextField(blank=True,null=True,name="description",verbose_name="Description")
    image=models.ImageField(upload_to='services',blank=True,null=True,name="image",verbose_name='Image')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')

    class Meta:
        ordering=['-created']
        verbose_name="Service"

    def __str__(self) -> str:
        return self.titre
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.titre)
        
        super().save(*args,**kwargs)

class Temoignage(models.Model):
    fullname=models.CharField(max_length=200,name="fullname",verbose_name="Full Name",blank=True,null=True)
    specialite=models.ForeignKey(Specialite,on_delete=models.CASCADE,verbose_name='Specialite',name='specialite',blank=True,null=True)
    photo=models.ImageField(upload_to='temoignage_photo',blank=True,null=True,name="photo",verbose_name='Photo')
    contenu=models.TextField(blank=True,null=True,verbose_name='Contenu',name='contenu')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Create date',name='created')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date',name='updated')
    
    class Meta:
        ordering=['-created']
        verbose_name="Temoignage"

    def __str__(self) -> str:
        return self.fullname

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)



class Team(models.Model):
    nom=models.CharField(max_length=200,name="nom",verbose_name="Nom")
    slug=models.SlugField(max_length=200,verbose_name='Slug')
    email=models.EmailField(blank=True,null=True,max_length=200,name="email",verbose_name="Email")
    phone=PhoneNumberField(null=True,blank=True,unique=True)
    specialite=models.ForeignKey(Specialite,on_delete=models.CASCADE,verbose_name='Specialite',name='specialite')
    grade=models.ForeignKey(Grade,on_delete=models.CASCADE,verbose_name='Grade',name='grade')
    description=models.TextField(blank=True,null=True,name="description",verbose_name="Description")
    photo=models.ImageField(upload_to='teams',blank=True,null=True,name="photo",verbose_name='Photo')
    twitter=models.CharField(blank=True,null=True,verbose_name="Twitter",max_length=200)
    facebook=models.CharField(blank=True,null=True,verbose_name="Facebook",max_length=200)
    instagram=models.CharField(blank=True,null=True,verbose_name="Instagram",max_length=200)
    linkdin=models.CharField(blank=True,null=True,verbose_name="Linkdin",max_length=200)
    created=models.DateTimeField(auto_now_add=True,verbose_name='Create date',name='created')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date',name='update')

    class Meta:
        verbose_name="Team"

    def __str__(self) -> str:
        return self.nom

# Contact
class Contact(models.Model):
    nom=models.CharField(blank=True,null=True,max_length=100,name='nom',verbose_name='Nom')
    email=models.EmailField(blank=True,null=True,max_length=100,name='email',verbose_name='Email')
    sujet=models.CharField(blank=True,null=True,max_length=100,name='sujet',verbose_name='Sujet')
    message=models.TextField(blank=True,null=True,verbose_name='Message',name='message')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Create date',name='created')
    
    class Meta:
        ordering=['-created']
        verbose_name="Contact"

    def __str__(self) -> str:
        return self.nom

class NewsLetter(models.Model):
    email=models.EmailField(blank=True,null=True,max_length=100,verbose_name='Email',name='email')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Date')
    
    class Meta:
        verbose_name="NewsLetter"
        ordering=['-created']

    def __str__(self) -> str:
        return self.email

# Blog
class BlogTags(models.Model):
    title=models.CharField(max_length=100)
    create_at=models.DateField(auto_now_add=True)
    
class Article(models.Model):
    tags=models.ForeignKey(BlogTags,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_blog_tags')
    titre=models.CharField(max_length=100,verbose_name='Titre')
    slug=models.SlugField(max_length=200,verbose_name='Slug')
    description1=models.CharField(max_length=200,blank=True,null=True,verbose_name="Description2")
    description2=QuillField(blank=True,null=True,max_length=200,verbose_name='description1')
    image=models.ImageField(upload_to='articles_images',blank=True,null=True,name="image",verbose_name='Image')
    auteur=models.ForeignKey(CustomerUser,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Auteur')
    categorie=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_categorie',
                                verbose_name='Categorie')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    published=models.BooleanField(default=False,verbose_name="Publie")

    class Meta:
        ordering=['-created']
        verbose_name="Article"

    def __str__(self) -> str:
        return self.titre

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.titre)
        
        super().save(*args,**kwargs)

class Commentaire(models.Model):
    blog=models.ForeignKey(BlogTags,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_blog_comment')
    content=models.TextField(blank=True,null=True,verbose_name='Commentaire')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    auteur=models.ForeignKey(CustomerUser,on_delete=models.CASCADE,blank=True,null=True,
                            related_name='fk_user_comment',
                            verbose_name='Auteur')
    
    class Meta:
        ordering=['-created']
        verbose_name="Commentaire"
    

class Slider(models.Model):
    titre=models.CharField(max_length=200,name="titre",verbose_name="Titre",blank=True,null=True)
    photo=models.ImageField(upload_to='slider',blank=True,null=True,name="photo",verbose_name='Photo')
    contenu=models.TextField(blank=True,null=True,verbose_name='Contenu',name='contenu')
    status=models.BooleanField(default='True',verbose_name='Status')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Create date',name='created')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date',name='updated')
    
    class Meta:
        ordering=['-created']
        verbose_name="Slider"

    def __str__(self) -> str:
        return self.titre

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
