from email.policy import default
from turtle import mode
from django.db import models

# Create your models here.

class Criminal(models.Model):
    crim_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to = "app1/images",default="")
    age = models.CharField(max_length=50,default="Not known")
    nationality = models.CharField(max_length=100,default="Not known")
    gender = models.CharField(max_length=20,default="Male")
    weight = models.CharField(max_length=50,default="Not known")
    height = models.CharField(max_length=50,default="Not known")
    isWanted = models.BooleanField(default=False)    
    wantedInCountry=models.CharField(max_length=100,default=" ")
    charges = models.CharField(max_length=1000,default="")
    about = models.CharField(max_length=10000,default="")

    def __str__(self):
        return self.name

'''
id
name
image
age
weight
plaeOfBirth
nationality
isWanted
gender
height
languageSpoken
charges
About
'''