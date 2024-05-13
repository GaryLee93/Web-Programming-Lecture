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
        return self.title