from django.db import models

class service_data(models.Model):
    service_icon = models.CharField(max_length=100)
    service_title = models.CharField(max_length=100)
    service_des = models.TextField()

# Create your models here.
