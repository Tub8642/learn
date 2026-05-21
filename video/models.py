from django.db import models
from django.utils.text import slugify

class Category


class Video(models.Model):
    name = models.CharField(max_length=200, verbose_name='') #nazvanie
    pub_date = models.DateTimeField('date published') #data publikacii
    video_url = models.URLField() #ssylka na video
    oblozhka_url = ???
