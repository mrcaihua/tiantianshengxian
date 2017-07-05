from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname=models.CharField(max_length=10)
    upwd=models.CharField(max_length=40)
    umail=models.CharField(max_length=20)
    uphone=models.CharField(max_length=11)
    uaddrss=models.CharField(max_length=100)
