from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=500,default='')
    email = models.EmailField(max_length=2000,default='')
    message = models.TextField(max_length=10000,default='')
