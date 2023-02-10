from django.db import models

# Create your models here.
# Developed by Surfa
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"publish")
)


class Bod(models.Model):
    title = models.CharField(max_length=200, unique=False)
    name = models.CharField(max_length=200, unique=True)
    about = models.CharField(max_length=200, unique=False)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    image2 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return self.title



class Contact(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, unique=True)
    message = models.TextField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name

User = get_user_model()
