from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models.myuser import MyUser


class SignupForm(forms.ModelForm):

    class Meta:
        # password1= forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":'Password 1'}))
        # password2= forms.CharField(widget=forms.PasswordInput({"placeholder":'password 2'}))
        model=MyUser
        fields=['first_name','last_name','username','email','password']

        widgets={"first_name":forms.TextInput({"placeholder":'First Name'}),
                'last_name':forms.TextInput({"placeholder":'Last Name'}),
                'username':forms.TextInput({"placeholder":'User Name'}),
                'email':forms.TextInput({'placeholder':'Email ','type':'email'}),
                'password':forms.PasswordInput({"placeholder":'Password'})}

