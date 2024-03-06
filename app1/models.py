from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Products(models.Model):
  product_name=models.CharField(max_length=50)
  product_price=models.IntegerField()

class Students(models.Model):
  #connection=models.OneToOneField(User,on_delete=models.CASCADE)
  stud_name=models.CharField(max_length=50)
  mothername=models.CharField(max_length=50)
  fathername=models.CharField(max_length=50)
  nationality=models.CharField(max_length=50)
  gender=models.CharField(max_length=1)
  address=models.TextField(max_length=50)
  dob=models.CharField(max_length=50)
  reserv=models.CharField(max_length=50)
  classstd=models.IntegerField() 

class Department(models.Model):
  dept_name=models.CharField(max_length=50) 

class Teacher(models.Model):
  connection=models.OneToOneField(User,on_delete=models.CASCADE)
  teach_name=models.CharField(max_length=50)
  teach_mob=models.CharField(max_length=50)
  teach_email=models.CharField(max_length=50)
  teach_dob=models.CharField(max_length=50)
  teach_joingdate=models.CharField(max_length=50)
  teach_dept=models.ForeignKey(Department,on_delete=models.CASCADE)
  teach_address=models.CharField(max_length=50)


 
