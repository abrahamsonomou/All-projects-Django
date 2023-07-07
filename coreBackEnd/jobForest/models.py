from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django_ckeditor_5.fields import CKEditor5Field
import uuid
from authentification.models import User

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Published")
)

class jCategory(models.Model): #Category for the Article
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False, unique=True) #Unique identifier for the Category
    title = models.CharField(max_length=200) #Title of the Category
    created_on = models.DateTimeField(auto_now_add=True) #Date of creation
    updated_on = models.DateTimeField(auto_now=True) #Date of updation
    status = models.IntegerField(choices=STATUS, default=0) #Status of the Article either Draft or Published

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title

class jBlogPost(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False, unique=True) #Unique identifier for the article
    title = models.CharField(max_length=200, unique=True) #Title of the Article
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True, related_name='jblog_posts') #Author of the Article
    description = models.TextField(blank=True,null=True) #Short Description of the article
    content = CKEditor5Field(config_name='extends') #Content of the article, you need to install CKEditor
    tags = TaggableManager() #Tags for a Particular Article, You need to install Taggit
    category = models.ForeignKey('jCategory', related_name='jblog_category', on_delete=models.CASCADE) #Category of the article
    keywords = models.CharField(max_length=500,blank=True,null=True) #Keywords to be used in SEO
    views = models.IntegerField(default=0)
    is_popular = models.BooleanField(default=False)
    image = models.ImageField(upload_to='jobForest/blog_images') #Cover Image of the article
    bg = models.ImageField(upload_to='jobForest/blog_background_images', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True) #Date of creation
    updated_on = models.DateTimeField(auto_now=True) #Date of updation
    status = models.IntegerField(choices=STATUS, default=0) #Status of the Article either Draft or Published

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jobforestBlogDetails", kwargs={'pk': self.pk})
    
    