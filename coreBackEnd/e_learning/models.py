from django.db import models
import uuid
from django.urls import reverse
from taggit.managers import TaggableManager
from django_ckeditor_5.fields import CKEditor5Field
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _ 
from authentification.models import User

# Create your models here.
class eCategory(TranslatableModel):
    translations = TranslatedFields(
    category_name=models.CharField(max_length=200,verbose_name="Category Name"),
    description=models.TextField(blank=True,null=True,verbose_name="Description"),
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date'),
    )
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    image=models.ImageField(upload_to='cours/Category',blank=True,null=True)
    active=models.BooleanField(default=True,verbose_name="status")
#
# class Category(models.Model):
#     uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
#     category_name=models.CharField(max_length=200,verbose_name="Category Name")
#     description=models.TextField(blank=True,null=True,verbose_name="Description")
#     created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
#     updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
#     active=models.BooleanField(default=True,verbose_name="status")

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
    
    def __str__(self) -> str:
        return self.category_name
        
class eSubCategory(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    category=models.ForeignKey(eCategory,on_delete=models.SET_NULL,
                               blank=True,
                               null=True,related_name="fk_category",
                               verbose_name="Category")
    image=models.ImageField(upload_to='cours/SubCategory',blank=True,null=True)
    sub_category_name=models.CharField(max_length=200,verbose_name="Category Name")
    description=models.TextField(blank=True,null=True,verbose_name="Description")
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    active=models.BooleanField(default=True,verbose_name="status")

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categorys'
    
    def __str__(self) -> str:
        return self.category_name
    
STATUS = (
    (0, "Draft"),
    (1, "Published")
)

class eBlogPost(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False, unique=True) #Unique identifier for the article
    title = models.CharField(max_length=200, unique=True) #Title of the Article
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True, related_name='blog_posts') #Author of the Article
    description = models.TextField(blank=True,null=True) #Short Description of the article
    content = CKEditor5Field(config_name='extends') #Content of the article, you need to install CKEditor
    category = models.ForeignKey(eCategory, related_name='category_blog', on_delete=models.CASCADE) #Category of the article
    tags = TaggableManager() #Tags for a Particular Article, You need to install Taggit
    views = models.IntegerField(default=0)
    is_popular = models.BooleanField(default=False)
    image = models.ImageField(upload_to='blog/images') #Cover Image of the article
    bg = models.ImageField(upload_to='blog/bg_images', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True) #Date of creation
    updated_on = models.DateTimeField(auto_now=True) #Date of updation
    status = models.IntegerField(choices=STATUS, default=0) #Status of the Article either Draft or Published
    active=models.BooleanField(default=True,verbose_name="status")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={'pk': self.pk})

# Contact
class eContact(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    nom=models.CharField(blank=True,null=True,max_length=100,name='nom',verbose_name='Nom')
    email=models.EmailField(blank=True,null=True,max_length=100,name='email',verbose_name='Email')
    message=models.TextField(blank=True,null=True,verbose_name='Message',name='message')
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')

    class Meta:
        ordering=['-updated']
        verbose_name="Contact" 

    def __str__(self) -> str:
        return self.nom

class eNewsLetter(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email=models.EmailField(blank=True,null=True,max_length=100,verbose_name='Email',name='email')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Date')
    
    class Meta:
        verbose_name="NewsLetter"
        ordering=['-created']

    def __str__(self) -> str:
        return self.email

# end contact

    

