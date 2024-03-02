from django import forms
from django.contrib.auth.forms import UserCreationForm
from cakeapp.models import Login,Owner,Client
from django.db import models

class LoginRegister(UserCreationForm):
    class Meta:
        model=Login
        fields=('username','password1','password2')


class Ownerform(forms.ModelForm):
    class Meta:
        model=Owner
        exclude=('user',)

class Userform(forms.ModelForm):
    class Meta:
        model=Client
        exclude=('user',)
