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
    pic = models.ImageField(upload_to='images/',default='')
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title
