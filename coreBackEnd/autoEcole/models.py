from django.db import models
import uuid
from django_quill.fields import QuillField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Permis(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    typePermis= models.CharField(max_length=100,blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')

    class Meta:
        verbose_name = "Permis"
        verbose_name_plural = "Permis"  

class Vehicule(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    immatriculation= models.CharField(max_length=100,blank=True, null=True)
    marque= models.CharField(max_length=100,blank=True, null=True)
    description=models.TextField()
    image=models.ImageField(upload_to="vehicules_images", height_field=None, width_field=None, max_length=None)
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')

    class Meta:
        verbose_name = "Vehicule"
        verbose_name_plural = "Vehicules"   

class Lecon(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    titre= models.CharField(max_length=300,blank=True, null=True)
    contenu=QuillField(blank=True,null=True)
    urlVideo=models.URLField(max_length=200)
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')

    class Meta:
        verbose_name = "Leçon"
        verbose_name_plural = "Leçons"

class Eleve(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    matricule=models.CharField(max_length=15,blank=True,null=True)
    nom= models.CharField(max_length=50)
    adresse= models.CharField(max_length=50)
    telephone=PhoneNumberField(null=True,blank=True,unique=True)
    photo=models.ImageField(upload_to='eleves/avatars',blank=True,null=True)

    permis=models.ForeignKey(Permis, on_delete=models.CASCADE)
    vehicule=models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    dateNaissance=models.DateField(auto_now=False, auto_now_add=False)
    dateInscription=models.DateField(auto_now=False, auto_now_add=False)
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')

    class Meta:
        verbose_name = "Eleve"
        verbose_name_plural = "Eleves"

class PaiementEleve(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    motif=models.TextField()
    montant=models.DecimalField( max_digits=5, decimal_places=2)
    datePaiement=models.DateField(auto_now=False, auto_now_add=False)
    eleve=models.ForeignKey(Eleve,null=True, blank=True, on_delete=models.SET_NULL,related_name="eleve_paiement")
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    
    class Meta:
        verbose_name = "Paiement_Eleve"
        verbose_name_plural = "Paiements_Eleve"

class Moniteur(models.Model):
    CHOIX_GRADE=(
        ('licence','Licence'),
        ('master','Master'),
        ('doctorat','Doctorat'),
        ('bts','BTS'),
        ('autres','Autres'),
    )

    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    matricule=models.CharField(max_length=15,blank=True,null=True)
    nom= models.CharField(max_length=50)
    adresse= models.CharField(max_length=50)
    telephone=PhoneNumberField(null=True,blank=True,unique=True)
    photo=models.ImageField(upload_to='moniteurs/avatars',blank=True,null=True)
    grade=models.CharField(choices=CHOIX_GRADE,max_length=200)

    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    
    class Meta:
        verbose_name = "Moniteur"
        verbose_name_plural = "Moniteurs"

class PaiementMoniteur(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    motif=models.TextField()
    montant=models.DecimalField( max_digits=5, decimal_places=2)
    datePaiement=models.DateField(auto_now=False, auto_now_add=False)
    moniteur=models.ForeignKey(Moniteur,null=True, blank=True, on_delete=models.SET_NULL,related_name="moniteur_paiement")
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    
    class Meta:
        verbose_name = "Paiement_Moniteur"
        verbose_name_plural = "Paiements_Moniteur"

class Cours(models.Model):
    eleve=models.ForeignKey(Eleve, on_delete=models.CASCADE)
    moniteur=models.ForeignKey(Moniteur, on_delete=models.CASCADE)
    lecon=models.ForeignKey(Lecon, on_delete=models.CASCADE)
    date=models.DateField(auto_now=False, auto_now_add=False)
    duree=models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    
    class Meta:
        verbose_name = "Cours"
        verbose_name_plural = "Cours"

# #Galerie
class Galerie(models.Model):
    titre=models.CharField(max_length=200,name="titre",verbose_name="Titre",blank=True,null=True)
    photo=models.ImageField(upload_to='galerie',blank=True,null=True,name="photo",verbose_name='Photo')
    status=models.BooleanField(default='True',verbose_name='Status')
    
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    
    class Meta:
        ordering=['-updated']
        verbose_name="Galerie"

    def __str__(self) -> str:
        return self.titre
    
# #FAQ
class FAQ(models.Model):
    titre=models.CharField(max_length=200,verbose_name="Titre")
    description=models.TextField(blank=True,null=True,name="description",verbose_name="Description")
    faqcourse=models.BooleanField(default='False',verbose_name='Status')

    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
    
    def __str__(self) -> str:
        return self.titre

# #SLIDER
class Slider(models.Model):
    titre=models.CharField(max_length=200,name="titre",verbose_name="Titre",blank=True,null=True)
    photo=models.ImageField(upload_to='slider',blank=True,null=True,name="photo",verbose_name='Photo')
    contenu=models.TextField(blank=True,null=True,verbose_name='Contenu',name='contenu')
    status=models.BooleanField(default='True',verbose_name='Status')
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    
    class Meta:
        ordering=['-created']
        verbose_name="Slider"

    def __str__(self) -> str:
        return self.titre

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

# #Temoignage
class Temoignage(models.Model):
    nom=models.CharField(max_length=200)
    contenu=models.TextField(blank=True,null=True)
    photo=models.ImageField(upload_to='Temoignage',blank=True,null=True,verbose_name='Poster')
    fonction=models.CharField(max_length=200,blank=True,null=True,)
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