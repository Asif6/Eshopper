from django import views
from django.shortcuts import render
from shop.forms import SignupForm

from shop.models.myuser import MyUser
from uuid import uuid4

class Signup(views.View):
    def get(self,request):

        fr=SignupForm()

        data={}
        data["form"]=fr

        return render(request,"signup.html",data)

    def post(self,request):

        fr=SignupForm(request.POST)
        error=None
        data={}
        data["form"]=fr

        
        isemail=request.POST.get('email')
        First_Name=request.POST.get('first_name')

        if MyUser.objects.filter(email=isemail).exists():
            error="This email is allrady exiset try diffrent email"

        
        if fr.is_valid():

            first_name=fr.cleaned_data['first_name']
            last_name=fr.cleaned_data['last_name']
            username=fr.cleaned_data['username']
            email=fr.cleaned_data['email']
            password=fr.cleaned_data['password']


            token=uuid4()


            createuser=MyUser(first_name=first_name,last_name=last_name,username=username,email=email,password=password,token=token)

            # print(createuser.token)
            createuser.save()

            return render(request,'index.html')
        data['error']=error
        data['first_name']=First_Name
        print(error)
        return render(request,"signup.html",data)
        


