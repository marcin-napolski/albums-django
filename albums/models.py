from django.db import models

# Create your models here.
class Album(models.Model):
    image = models.ImageField(upload_to='images/')
    artist = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=200)