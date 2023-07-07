from main.models import *

# Create your models here.
class Tutoriel(BaseModel):
    titre=models.CharField(max_length=100,verbose_name='Titre')
    slug=models.SlugField(max_length=200,verbose_name='Slug',blank=True,null=True)
    description=models.TextField(blank=True,null=True,name="description",verbose_name="Description")
    image=models.ImageField(upload_to='tutoriels',blank=True,null=True,name="image",verbose_name='Poster')
    auteur=models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_user_tuto',
                                verbose_name='Auteur')
    categorie=models.ForeignKey(ArticleCategorie,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_category_tuto',
                                verbose_name='Category')
    url=EmbedVideoField(blank=True,null=True)
    published=models.BooleanField(default=False,verbose_name="Status")
    plublish=models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name="Tutoriel"
        ordering=['-updated']


    def __str__(self) -> str:
        return self.titre
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.titre)
        
        super().save(*args,**kwargs)
