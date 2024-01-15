from django import forms
from .models import *
class registerform(forms.Form):
    usrnm=forms.CharField(max_length=20)
    email = forms.EmailField()
    mob = forms.IntegerField()
    dob = forms.DateTimeField()
    qual = forms.CharField(max_length=20)
    pas = forms.CharField(max_length=20)
    cpas = forms.CharField(max_length=20)

class loginform(forms.Form):
    usrname = forms.CharField(max_length=20)
    pwd = forms.CharField(max_length=20)

class jpostform(forms.Form):
    cname=forms.CharField(max_length=20)
    cmail=forms.EmailField()
    jtitle=forms.CharField(max_length=20)
    wtype=forms.CharField(max_length=20)
    exp = forms.CharField(max_length=20)
    jtype = forms.CharField(max_length=20)

class job_apply(forms.Form):
    comname=forms.CharField(max_length=20)
    dsgn=forms.CharField(max_length=20)
    name=forms.CharField(max_length=20)
    mail=forms.EmailField()
    qual=forms.CharField(max_length=20)
    phone=forms.IntegerField()
    exp=forms.CharField(max_length=20)
    file=forms.FileField()

class mailform(forms.Form):
    username=forms.CharField(max_length=20)
    email=forms.EmailField()
    subject = forms.CharField(max_length=20)
    message=forms.CharField(max_length=500)




