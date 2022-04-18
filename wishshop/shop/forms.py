from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models.myuser import MyUser


class SignupForm(UserCreationForm):
    password1= forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":'Password 1'}))
    password2= forms.CharField(widget=forms.PasswordInput({"placeholder":'password 2'}))

    class Meta:

        model=MyUser
        fields=['first_name','last_name','username','email','password1','password2'] # We can ignore default fields from hare

        widgets={"first_name":forms.TextInput({"placeholder":'First Name'}),
                'last_name':forms.TextInput({"placeholder":'Last Name'}),
                'username':forms.TextInput({"placeholder":'User Name'}),
                'email':forms.TextInput({'placeholder':'Email ','type':'email'}),}
                # 'password1':forms.PasswordInput({"placeholder":'Password 1'}),
                # 'password2':forms.PasswordInput({"placeholder":'Password 2'}),}

