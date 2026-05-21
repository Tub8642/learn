from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='')

class Video(models.Model):
    name = models.CharField(max_length=200, verbose_name='') #nazvanie
    pub_date = models.DateTimeField('date published') #data publikacii
    video_url = models.URLField() #ssylka na video
    oblozhka_url = models.URLField()

class Meta:
    ordering = ['category', '-published']

def _str__(self):
    return self.title
