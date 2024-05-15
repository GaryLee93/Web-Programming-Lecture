from django.db import models
from django.utils import timezone

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
    research = models.CharField(max_length=50)
    lectures = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    slug = models.CharField(max_length=10)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name