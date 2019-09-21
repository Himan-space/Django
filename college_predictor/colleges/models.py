from django.db import models
from django import forms

class College_Details(models.Model):
    College_name=models.CharField(max_length=100)
    Address=models.TextField()
    City=models.CharField(max_length=20)
    State=models.CharField(max_length=20)
    Contact_no=models.CharField(max_length=50)
    Cut_off=models.PositiveIntegerField()

    def __str__(self):
        return self.College_name