from distutils.command.upload import upload
from django.db import models


class movie(models.Model):

    name = models.CharField( max_length=50)
    year = models.IntegerField()
    desc = models.CharField(max_length=250)
    img = models.ImageField(upload_to='gallery')
    
    
def __str__(self):
    return self.name
