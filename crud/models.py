from django.db import models

# Create your models here.
class Student(models.Model):
    name =models.CharField(max_length=255)
    department =models.CharField(max_length=255)
    roll=models.IntegerField()