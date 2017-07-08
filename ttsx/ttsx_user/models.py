from django.db import models


class UserInfo(models.Model):
    uname=models.CharField(max_length=10)
    upwd=models.CharField(max_length=40)
    umail=models.CharField(max_length=20)
    uphone=models.CharField(default='',max_length=11)
    uaddrss=models.CharField(default='',max_length=100)
    ucode=models.CharField(default='',max_length=6)
    ushow=models.CharField(default='',max_length=10)


