from django.db import models
from django import forms
from django.contrib.auth.models import User

class Student_Details(models.Model):
    image=models.ImageField(default="profile_images/no_image.png",upload_to='profile_images')
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Username=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    City=models.CharField(max_length=20)
    State=models.CharField(max_length=20)
    Department=models.CharField(max_length=20)
    Marks=models.DecimalField(max_digits=100, decimal_places=2,blank=False,null=False)
    
    def __str__(self):
        return self.FirstName
