from django.db import models
from tinymce.models import HTMLField

class about_data(models.Model):
    about_des = HTMLField()
    experience = models.IntegerField()
    chefc = models.IntegerField()

class members(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
# Create your models here.
