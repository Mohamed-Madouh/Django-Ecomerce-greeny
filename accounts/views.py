from django.shortcuts import render , redirect
from .models import Profile
from .forms import Signupform
from django.contrib.auth import authenticate , login

# Create your views here.


def singnup(request):
    if request.method == 'Post':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save
            username= form.cleaned_data['username']
            passworde= form.cleaned_data['password']
            user = authenticate(username = username , password=passworde)
            login(request,user)
            return redirect('/account/profile')
    else:
        form = Signupform
    return render(request,'registration/signup.html',{'form' :form})
     



def profile(request): 
    profile = Profile.objects.get(user=request.user)
    return render(request,'profile/profile.html',{'profile':profile})
 
     
def profile_edit(request):
    pass