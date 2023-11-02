from django.shortcuts import render,redirect
from .models import *
from . forms import CustomUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def register(request):
    form = CustomUserForm()
    if request.method =='POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form':form}
    return render(request,'auth/register.html',context)

def loginview(request):
    if request.method == "POST":
        name = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user =authenticate(request,username = name,password = pass1)

        if user is not None:
            login(request,user)
            messages.success(request,"Logged i successfully")
            return redirect('/')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('login')

    return render(request,'auth/login.html')

def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    

