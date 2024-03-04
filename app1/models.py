from django.db import models

# Create your models here.

class Products(models.Model):
  product_name=models.CharField(max_length=50)
  product_price=models.IntegerField()

class Students(models.Model):
  stud_name=models.CharField(max_length=50)
  mothername=models.CharField(max_length=50)
  fathername=models.CharField(max_length=50)
  nationality=models.CharField(max_length=50)
  gender=models.CharField(max_length=1)
  address=models.TextField(max_length=50)
  dob=models.CharField(max_length=50)
  reserv=models.CharField(max_length=50)
  classstd=models.IntegerField()  
