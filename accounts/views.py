from django.shortcuts import render , redirect
from django.core.mail import send_mail
from .forms import Signupform ,UserActivateForm
from .models import Profile


# Create your views here.


def singnup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            
            username= form.cleaned_data['username']
            email= form.cleaned_data['email']
            form.save()
            
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
            return redirect(f'/account/{username}/activate')
    else:
        form = Signupform()
    return render(request,'registration/signup.html',{'form' :form})
     
def user_activate(request,username):
    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form = UserActivateForm(request.POST)
        if form.is_valid():
           code =form.cleaned_data['code']
           if profile.code == code:
               profile.active = True
               profile.code =''
               profile.code_used = True
               return redirect('/account/login')
            
        
    else:
        form = UserActivateForm()
    return render(request,'registration/activation.html',{'form':form})
       
    


def profile(request): 
    
    return render(request,'profile/profile.html',{'Profile':profile})
 
     
def profile_edit(request):
    pass