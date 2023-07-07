from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.contrib.auth.models import BaseUserManager
import uuid
from django.utils.translation import gettext_lazy as _ 

# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        
        if not email:
            raise ValueError('Desolé, veuillez saisir un email')
        
        email=self.normalize_email(email)
        user=self.model(email=email,username=username)
        
        user.set_password(password)
        
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password):
        user=self.create_user(email,username,password)
        
        user.is_staff=True
        user.is_active=True
        user.is_superuser=True
        
        user.save(using=self._db)
        return user   

class User(AbstractUser):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    username = models.CharField(max_length=50, default='Anonymous', unique=True)
    email = models.EmailField(db_index=True,max_length=254, unique=True,blank=True,null=True)
    # username = None 
    last_name = models.CharField(max_length=250, blank=True, null=True)
    first_name = models.CharField(max_length=250, blank=True, null=True)
    midle_name = models.CharField(max_length=250, blank=True, null=True)

    session_token = models.CharField(max_length=10, default=0,blank=True,null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_active=models.BooleanField(default=True,blank=True,null=True)
    is_staff=models.BooleanField(default=False,blank=True,null=True)

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    photo = models.ImageField(upload_to='users/photos/',blank=True, null=True)


    # USERNAME_FIELD='email'
    # REQUIRED_FIELDS=['username']

    USERNAME_FIELD='username'
    # REQUIRED_FIELDS=['username']
    
    objects= UserProfileManager()
    
    class Meta:
        verbose_name=_("Utilisateur")

    def __str__(self):
        if self.is_student:
                type_ = 'Student'
        elif self.is_teacher:
            type_ = 'Teacher'
        else:
            type_ = 'None'
        return f'{type_}: {self.email}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            pic = Image.open(self.photo.path)
            if pic.width > 256:
                pic.thumbnail((256, pic.height / (pic.width / 265)))
                pic.save(self.photo.path)


    def get_photo_url(self):
        if self.photo:
            return self.photo.url
        else:
            if self.is_student:
                return '/media/users/students/student-default.png'
            elif self.is_teacher:
                return '/media/users/teachers/teacher-default.png'
            else:
                return '/media/users/default.png'

    def get_photo_name(self):
        if self.photo:
            return self.photo.name 
        else:
            if self.is_student:
                return 'student-default.png'
            elif self.is_teacher:
                return 'teacher-default.png'
            else:
                return 'default.png'

    def get_profile(self):
        if self.is_student:
            return Student.objects.get(user=self)
        elif self.is_teacher:
            return Teacher.objects.get(user=self)
        else:
            return None

    def get_shortname(self):
        return f'{self.first_name[0:1]}.{self.last_name}'

    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'
        
    objects= UserProfileManager()

class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True)
	interested_category=models.TextField(blank=True,null=True,verbose_name="Interested category")
	
	def __str__(self) -> str:
		return f'{self.user.email}'

class Teacher(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True)
	
	def __str__(self) -> str:
		return f'{self.user.email}'