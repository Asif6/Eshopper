import email
from lib2to3.pgen2 import token
from re import T
from turtle import mode
from django.contrib.auth.models import User,AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.db import models
import uuid

from django.forms import EmailField
import uuid


class MyUserManager(BaseUserManager):
    use_in_migrations=True

    def create_user(self,first_name,last_name,email,password=None,**extra_fields):

        if not first_name:
            raise ValueError("First name is required")
        if not last_name:
            raise ValueError("Last name is required")
        if not email:
            raise ValueError("Email is required")
        
        email=self.normalize_email(email=email)
        user=self.model(first_name=first_name,last_name=last_name,email=email,**extra_fields)
        user.set_password(raw_password=password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,email,password=None,**extra_fields):
        extra_fields.setdefault("is_active",True)
        extra_fields.setdefault("is_admin",True)
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)

        return self.create_user(first_name,last_name,email,password,**extra_fields)




class MyUser(AbstractBaseUser,PermissionsMixin):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=70)
    token=models.CharField(max_length=1000)
    email_verify=models.BooleanField(default=False)

    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    objects=MyUserManager()


    USERNAME_FIELD='email'
    EmailField="email"

    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        return self.email

    def get_fullname(self):
        return str(self.first_name) +" "+ str(self.last_name)

