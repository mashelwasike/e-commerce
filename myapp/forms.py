from django.shortcuts import render,redirect 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from .models import User

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-3','placeholder':'Username'}))
    email =forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control my-3','placeholder':'Email'}))
    password1 =forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-3','placeholder':'Enter Password'}))
    password2 =forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']