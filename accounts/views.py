from django.shortcuts import render , redirect
from django.core.mail import send_mail
from .forms import Signupform
from .models import Profile

from django.contrib.auth import authenticate , login

# Create your views here.


def singnup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            
            username= form.cleaned_data['username']
            email= form.cleaned_data['password']
            myform = form.save()
            profile = Profile.objects.get(user__username=username)
            profile.active=False
            profile.save()
            #send email
            send_mail(
                subject="Activate Your Account",
                message=f"use this code {{profile.code}} to activate your account .",
                from_email="mm9073595@gmail.com",
                recipient_list=[email],
                fail_silently=False
            )
    else:
        form = Signupform()
    return render(request,'registration/signup.html',{'form' :form})
     
def user_activate(request):
    pass


def profile(request): 
    profile = Profile.objects.get(user=request.user)
    return render(request,'profile/profile.html',{'Profile':profile})
 
     
def profile_edit(request):
    pass