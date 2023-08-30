from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User



class Signupform(UserChangeForm):
     class Meta:
         model = User
         fields = ['username','email','password',]








class UserActivateForm(forms.Form):
    code = forms.CharField(max_length=8)