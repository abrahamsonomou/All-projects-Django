
# Create your models here.
from django_quill.fields import QuillField
from django.template.defaultfilters import slugify
from phonenumber_field.modelfields import PhoneNumberField
from app_auth.models import *
from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Categorie(models.Model):
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
        
class Portfolio(models.Model):
    titre=models.CharField(max_length=100,verbose_name='Titre')
    slug=models.SlugField(blank=True,null=True,max_length=200,verbose_name='Slug')
    date_projet=models.DateField(blank=True,null=True,max_length=100,verbose_name='Date projet')
    url=models.URLField(blank=True,null=True,max_length=100,verbose_name='Url')
    client=models.CharField(blank=True,null=True,max_length=100,verbose_name='Client')
    description=models.TextField(blank=True,null=True,max_length=1000,verbose_name='Description')
    image=models.ImageField(upload_to='Portfolios_images',blank=True,null=True,name="image",verbose_name='Image')
    image1=models.ImageField(upload_to='Portfolios_images',blank=True,null=True,name="image1",verbose_name='Image1')
    image2=models.ImageField(upload_to='Portfolios_images',blank=True,null=True,name="image2",verbose_name='Image2')
    image3=models.ImageField(upload_to='Portfolios_images',blank=True,null=True,name="image3",verbose_name='Image3')
    categorie=models.ForeignKey(Categorie,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_categorie_portfolio',
                                verbose_name='Categorie')
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
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
            
# teams
class Specialite(models.Model):
    nom_specialite=models.CharField(name='nom_specialite',verbose_name='Nom_specialite',max_length=200)

    class Meta:
        verbose_name="Specialite"

    def __str__(self) -> str:
        return self.nom_specialite


class Grade(models.Model):
    nom_grade=models.CharField(name='nom_grade',verbose_name='nom_grade',max_length=200)

    class Meta:
        verbose_name="Grade"

    def __str__(self) -> str:
        return self.nom_grade

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
    email=models.EmailField(blank=True,null=True,max_length=200,name="email",verbose_name="Email",unique=True)
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

# Blog
class BlogTags(models.Model):
    title=models.CharField(max_length=100)
    create_at=models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
class Article(models.Model):
    CHOIX_STATUT={
        ('publie','publié'),
        ('corbeille','corbeille'),
    }
    # tags=models.ForeignKey(BlogTags,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_blog_tags')
    titre=models.CharField(max_length=100,verbose_name='Titre')
    slug=models.SlugField(max_length=200,verbose_name='Slug')
    description1=models.CharField(max_length=200,blank=True,null=True,verbose_name="Description1")
    description2=QuillField(blank=True,null=True,max_length=200,verbose_name='Description2')
    image=models.ImageField(upload_to='articles_images',blank=True,null=True,name="image",verbose_name='Image')
    user=models.ForeignKey(CustomerUser,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Auteur')
    categorie=models.ForeignKey(Categorie,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_categorie',
                                verbose_name='Categorie')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    published=models.CharField(max_length=200,choices=CHOIX_STATUT,default="corbeille",verbose_name="Statut")

    class Meta:
        ordering=['-created']
        verbose_name="Article"

    def __str__(self) -> str:
        return self.titre

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.titre)
        
        super().save(*args,**kwargs)
        
    def get_absolute_url(self):
        return reverse("mes_articles")
    
class Commentaire(models.Model):
    blog=models.ForeignKey(BlogTags,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_blog_comment')
    content=models.TextField(blank=True,null=True,verbose_name='Commentaire')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    user=models.ForeignKey(CustomerUser,on_delete=models.CASCADE,blank=True,null=True,
                            related_name='fk_user_comment',
                            verbose_name='Auteur')
    
    class Meta:
        ordering=['-created']
        verbose_name="Commentaire"