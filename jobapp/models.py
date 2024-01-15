from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class profile1(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=20)
    is_verified=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class regimodel(models.Model):
    musr=models.CharField(max_length=20)
    memail=models.EmailField()
    mmob=models.IntegerField()
    mdob=models.DateTimeField()
    mqual=models.CharField(max_length=20)
    mpas=models.CharField(max_length=20)

class jpostmodel(models.Model):
    wtyp = [
        ('remote','remote'),
        ('hybrid','hybrid')
    ]
    jtyp = [
        ('half time','half time'),
        ('full time','full time')
    ]
    jexp = [
        ('0-1','0-1'),
        ('1-2', '1-2'),
        ('2-3', '2-3'),
        ('3-4', '3-4'),
        ('4-5', '4-5'),
        ('5-6', '5-6'),
        ('6-7', '6-7')
    ]

    cname=models.CharField(max_length=20)
    cemail=models.EmailField()
    ctitle=models.CharField(max_length=20)
    cwtyp=models.CharField(max_length=20,choices=wtyp)
    cjtyp=models.CharField(max_length=20,choices=jtyp)
    cjexp=models.CharField(max_length=10,choices=jexp)

class japp(models.Model):
    ecom=models.CharField(max_length=20)
    edsgn=models.CharField(max_length=20)
    ename=models.CharField(max_length=20)
    eemail=models.EmailField()
    equal=models.CharField(max_length=20)
    eph=models.IntegerField()
    eexp=models.CharField(max_length=20)
    resume = models.FileField(upload_to="jobapp/static")



