from pyexpat import model
from django.db import models

# Create your models here.
class firstmigration(models.Model):
    username=models.CharField(max_length=10)
    phone_number=models.IntegerField()
    email=models.EmailField()