from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField()
    city=models.CharField(max_length=20)
    datetime_data=models.DateTimeField(null=True,blank=True)

class Studentclean(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField()
    city=models.CharField(max_length=20)
    datetime_data = models.DateTimeField(null=True, blank=True)


