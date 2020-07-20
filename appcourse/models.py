from django.db import models
import  datetime
import time
import datetime


# Create your models here.

class centermodel(models.Model):
    no =  models.AutoField(primary_key=True)
    course_name= models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=25)
    fee = models.IntegerField()
    duration = models.CharField(max_length=50)

class studentregistration(models.Model):
    num = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Contactno = models.IntegerField(unique=True)
    Email =  models.EmailField(unique=True,max_length=60)
    Password = models.CharField(max_length=30)

class Enroll(models.Model):

    course_name = models.CharField(max_length=50)
    Contactno = models.IntegerField(unique=True)

