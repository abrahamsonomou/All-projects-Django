from django.db import models
import uuid
from app_auth.models import CustomerUser
from django.template.defaultfilters import slugify
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')

    class Meta:
        abstract=True
        
class Evenement(BaseModel):
    titre_event=models.CharField(max_length=200,verbose_name="Nom de l'evenement")
    slug=models.SlugField(max_length=200,verbose_name='Slug',blank=True,null=True)
    description=models.TextField(blank=True,null=True,name="description",verbose_name="Description")
    image=models.ImageField(upload_to='events_images',blank=True,null=True,verbose_name='Poster')
    lien=models.URLField(blank=True,null=True,verbose_name='Lien')
    lieu=models.CharField(max_length=100,verbose_name='Lieu')
    heure=models.TimeField(blank=True,null=True,max_length=100,verbose_name='Heure')
    dateEv=models.DateField(blank=True,null=True,verbose_name='Date')
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Evenement'
        verbose_name_plural = 'Evenements'
    
    def __str__(self) -> str:
        return self.titre_event

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.titre_event)
        
        super().save(*args,**kwargs)
        
class Reglement(models.Model):
    titre_reglement=models.CharField(max_length=200,verbose_name="Titre")
    slug=models.SlugField(max_length=200,verbose_name='Slug',blank=True,null=True)
    description=models.TextField(blank=True,null=True,name="description",verbose_name="Description")
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Reglement'
        verbose_name_plural = 'Reglements'
    
    def __str__(self) -> str:
        return self.titre_reglement

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.titre_reglement)
        
        super().save(*args,**kwargs)
        
class Bureau(BaseModel):
    fonction=models.CharField(max_length=200,verbose_name="Fonction")
    memdat=models.CharField(max_length=200,verbose_name="Memdat")
    membre=models.ForeignKey(CustomerUser,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Membre',related_name="fk_membre_bureau")

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Bureau'
        verbose_name_plural = 'Bureau'
    
    def __str__(self) -> str:
        return self.fonction

class Cotisation(BaseModel):
    MODE_PAYEMENT={
        ('espece','Espece'),
        ('transfere_flooz','FlOOZ'),
        ('transfere_tmoney','TMONEY'),
    }
    motif=models.CharField(max_length=200,verbose_name="Motif")
    membre=models.ForeignKey(CustomerUser,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Membre',related_name="fk_membre_cotisation")
    montant=models.DecimalField(decimal_places=2,max_digits=20)
    mode_payement=models.CharField(max_length=200,verbose_name="Mode de payement",choices=MODE_PAYEMENT)
    telephone=PhoneNumberField(null=True,blank=True)
    tx_reference=models.CharField(blank=True,null=True,max_length=2000)
    statut=models.BooleanField(default=False,blank=True,null=True)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Cotisation'
        verbose_name_plural = 'Cotisations'
    
    def __str__(self) -> str:
        return self.motif

class Contacts(BaseModel):
    nom=models.CharField(blank=True,null=True,max_length=100,name='nom',verbose_name='Nom')
    email=models.EmailField(blank=True,null=True,max_length=100,name='email',verbose_name='Email')
    message=models.TextField(blank=True,null=True,verbose_name='Message',name='message')
    
    class Meta:
        ordering=['-created']
        verbose_name="Contact"

    def __str__(self) -> str:
        return self.nom        

# blog
class Categorie(BaseModel):
    nom_categorie=models.CharField(max_length=100,verbose_name='Non categorie')
    slug=models.SlugField(max_length=200,verbose_name='Slug')

    class Meta:
        verbose_name="Categorie"

    def __str__(self) -> str:
        return self.nom_categorie
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.nom_categorie)
        
        super().save(*args,**kwargs)
        
class Article(BaseModel):
    titre=models.CharField(max_length=100,verbose_name='Titre')
    slug=models.SlugField(max_length=200,verbose_name='Slug')
    description=models.CharField(max_length=200,blank=True,null=True,verbose_name="Description")
    image=models.ImageField(upload_to='articles_images',blank=True,null=True,name="image",verbose_name='Image')
    user=models.ForeignKey(CustomerUser,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Auteur')
    categorie=models.ForeignKey(Categorie,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_categorie',
                                verbose_name='Categorie')
    statut=models.BooleanField(default=False,verbose_name="Statut")

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
    
class Commentaire(BaseModel):
    article=models.ForeignKey(Article,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_blog_comment')
    content=models.TextField(blank=True,null=True,verbose_name='Commentaire')
    user=models.ForeignKey(CustomerUser,on_delete=models.CASCADE,blank=True,null=True,
                            related_name='fk_user_comment',
                            verbose_name='Auteur')
    
    class Meta:
        ordering=['-created']
        verbose_name="Commentaire"
        
