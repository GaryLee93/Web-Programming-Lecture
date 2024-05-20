from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class News(models.Model):
    tag = models.CharField(max_length=10)
    body = models.CharField(max_length=50)
    uploadTime = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-uploadTime',)

    def __str__(self):
        return self.tag
    
class Professor(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=10)
    pic = models.ImageField(upload_to='images/',default='')
    research = models.CharField(max_length=50)
    lectures = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    slug = models.CharField(max_length=10)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class course(models.Model):
    name = models.CharField(max_length=50)
    slug = models.IntegerField(unique=True)
    time = models.CharField(max_length=20)
    credit = models.IntegerField()
    description = models.TextField(max_length=400)
    sweetScale = models.IntegerField(validators=[MinValueValidator(-1),MaxValueValidator(5)])

    def __str__(self):
        return self.name

class facility(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(3)])
    description = models.TextField(max_length=400)
    pic = models.ImageField(upload_to='facilities/',default='')

    def __str__(self):
        return self.name