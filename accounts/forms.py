from django import forms
from django.contrib.auth.forms import UserChangeForm ,UserCreationForm
from django.contrib.auth.models import User



class Signupform(UserChangeForm , UserCreationForm):
     class Meta:
         model = User
         fields = ['username','email','password1','password2']








class UserActivateForm(forms.Form):
    code = forms.CharField(max_length=8)