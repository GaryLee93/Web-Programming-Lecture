from django.core.validators import MinValueValidator 
from django.utils import timezone
from django.db import models
import os
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    abstract = models.IntegerField(
        verbose_name='abstract',
        default=20,
        validators=[MinValueValidator(0)]
    )
    body = models.TextField()
    pic = models.ImageField(upload_to='images/',default='',blank=True)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

class Mood(models.Model):
    status = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.status

class MoodPost(models.Model):
    mood = models.ForeignKey('Mood',on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50,default="不告訴你")
    message = models.TextField(null=False)
    del_pass = models.CharField(max_length=50)
    pub_time = models.DateTimeField(default=timezone.now)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.message
