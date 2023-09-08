from django.db import models
from django.db.models import Model

# Create your models here.
class Mclip(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to ='hcapp/media/')

class Mpic(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to ='pics')
