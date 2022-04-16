from django import views
from django.shortcuts import render


class Login(views.View):
    def get(self,request):

        return render(request,'login.html')