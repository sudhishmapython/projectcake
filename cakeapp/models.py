from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_owner=models.BooleanField(default=False)
    is_user=models.BooleanField(default=False)


class Owner(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    phone_no=models.IntegerField()

class Client(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    phone_no = models.IntegerField()
