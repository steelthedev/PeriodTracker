from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth import login,logout
# Create your views here.

def SignupView(request):
  if request.method=="POST":
    form=Signup(request.POST)
    if form.is_valid():
      user=form.save()
      user.refresh_from_db()
      user.profile.first_name=form.cleaned_data.get('first_name')
      user.profile.last_name=form.cleaned_data.get('last_name')
      user.profile.email=form.cleaned_data.get('email')
      user.save()
      
      template=render_to_string('accounts/welcome.html',{'name':user.profile.first_name})
      
      email=user.profile.email    
      send_mail(
        'Welcome to Ingenious Period Web App',
        template,
        settings.EMAIL_HOST_USER,
        ['email'],
        fail_silently=False)
      return redirect('period:main')

    
  else:
    form=Signup()
            
  return render(request,'accounts/signup.html',{'form':form})


def LoginView(request):
  if request.method=="POST":
    form=Login(data=request.POST)
    if form.is_valid():
      user=form.get_user()
      login(request,user)
      return redirect('dashboard:dash_home')
  else:
    form=Login()
  return render(request,'accounts/signin.html',{'form':form})

def LogoutView(request):
  logout(request)
  return redirect('period:main')