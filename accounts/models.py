from django.db import models
from django.utils.text import slugify

# Create your models here.

def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "job/%s.%s"%(instance.id,instance.id,extension)



class job(models.Model):
    owner = models.ForeignKey('auth.User', related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100) #column
    #location
    JOB_TYPE =(
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
    )
    job_type = models.CharField(max_length=15, choices=JOB_TYPE) #dropdown
    description = models.TextField(max_length=1000) #textarea
    published_at = models.DateTimeField(auto_now=True) #date
    vacancy = models.IntegerField(default=1) #number    
    salary = models.IntegerField(default=0) #number
    experience = models.IntegerField(default=1) #number
    category =models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='jobs/') #image

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(job, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    


class Apply(models.Model):
    job = models.ForeignKey(job, on_delete=models.CASCADE, related_name='apply_job')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name    