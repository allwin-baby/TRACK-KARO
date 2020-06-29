from django.db import models

# Create your models here.

class Login(models.Model):
    username= models.CharField(max_length=10)
    password= models.CharField(max_length=10)
    rollid  = models.IntegerField()

 


class User(models.Model):
    loginid= models.ForeignKey(Login,on_delete=models.CASCADE)
    name= models.CharField(max_length=20)
    email = models.CharField(max_length=30)
   