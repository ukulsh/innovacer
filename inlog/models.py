# Create your models here.
from django.db import models

class Visitor(models.Model):
    name = models.TextField(max_length=30)
    email = models.TextField(max_length=30)
    host = models.TextField(max_length=30)
    inTime = models.DateTimeField(auto_now_add=True)




class Host(models.Model):
    name = models.TextField(max_length=30)
    email = models.TextField(max_length=30)
    outtime = models.DateTimeField(auto_now_add=True)
