from django.db import models

# Create your models here.
class job(models.Model):
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
    nick_name = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name