from main.models import *

# Create your models here.
# la class personne
class Personne(BaseModel):
    full_name=models.CharField(blank=True,null=True,max_length=2000,verbose_name="Full name")
    email=models.CharField(blank=True,null=True,max_length=2000,verbose_name="Email")
    adresse=models.CharField(blank=True,null=True,max_length=2000,verbose_name="Adresse")
    telephone=PhoneNumberField(null=True,blank=True,unique=True)
    qualification=models.CharField(blank=True,null=True,verbose_name="Qualification",max_length=200,)
    password=models.CharField(blank=True,null=True,verbose_name="password",max_length=200,)
    description=models.TextField(blank=True,null=True,verbose_name="Description")
    
    class Meta:
        abstract=True

    def __str__(self) -> str:
        return self.full_name
    
# la class teacher
class Teacher(Personne):
    photo=models.ImageField(upload_to='teachers_avatar',blank=True,null=True,verbose_name='Photo')

    class Meta:
        verbose_name="Teacher"
            
# la class Competence
class Competence(BaseModel):
    title=models.CharField(verbose_name='Title',max_length=200)
    pourcentage=models.IntegerField(null=True,blank=True,verbose_name="Pourcentage")
    teacher=models.ForeignKey(Teacher,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Teacher',related_name="fk_teacher_competence")
    
    class Meta:
        verbose_name="Competence"

    def __str__(self) -> str:
        return self.title
    
# la class student   
class Student(Personne):
    photo=models.ImageField(upload_to='students_avatar',blank=True,null=True,verbose_name='Photo')
    interested_category=models.TextField(blank=True,null=True,verbose_name="Interested category")

    class Meta:
        verbose_name="Student"

# la class BaseCourse
class BaseCourse(BaseModel):
    title=models.CharField(max_length=200,verbose_name="Title")
    slug=models.SlugField(max_length=200,verbose_name='Slug',blank=True,null=True)
    description=models.TextField(blank=True,null=True,verbose_name="Description")
   
    class Meta:
        abstract=True
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        
        super().save(*args,**kwargs) 
    
    def __str__(self) -> str:
        return self.title    
       
# la class coursecategory    
class CourseCategory(BaseCourse):
    image=models.ImageField(upload_to='categorys_images',blank=True,null=True,verbose_name='Image')

    class Meta:
        verbose_name = 'Category Cours'
        verbose_name_plural = 'Categorys Cours'
    
# la class course    
class Cours(BaseCourse):
    image=models.ImageField(upload_to='cours_images',blank=True,null=True,verbose_name='Image')
    prix=models.DecimalField(decimal_places=2,max_digits=20)
    category=models.ForeignKey(CourseCategory,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Category',related_name="fk_category")
    teacher=models.ForeignKey(Teacher,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Teacher',related_name="fk_teacher")

    class Meta:
        verbose_name = 'Cours'
        verbose_name_plural = 'Cours'
        