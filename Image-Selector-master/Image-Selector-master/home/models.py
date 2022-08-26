from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField
    name=models.CharField(max_length=10,blank=True,null=True)
    education=models.CharField(max_length=10,blank=True,null=True)
    location=models.CharField(max_length=10,blank=True,null=True)
    living_in=models.CharField(max_length=10,blank=True,null=True)
    occupation=models.CharField(max_length=10,blank=True,null=True)
    annual_income=models.CharField(max_length=10,blank=True,null=True)
    comments=models.CharField(max_length=10,blank=True,null=True)
    age=models.CharField(max_length=10,blank=True,null=True)
    sex=models.CharField(max_length=10,blank=True,null=True)
    email=models.CharField(max_length=255, unique=True)
    curr_location=models.CharField(max_length=10,blank=True,null=True)
    ip_address=models.CharField(max_length=10,blank=True,null=True)
    email=models.CharField(max_length=10,blank=True,null=True)

