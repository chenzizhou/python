from distutils.command.upload import upload
from django.db import models
# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=10)
    age=models.IntegerField()
    job=models.CharField(max_length=30)
    sal=models.FloatField(max_length=10)
    address=models.CharField(max_length=30)
    photo=models.ImageField(upload_to='index/static/img',null=True)

    
