from django.db import models
from django.forms import CharField

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=25)
    ISBN = models.CharField(max_length=13)
    subtitle = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title