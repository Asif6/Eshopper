from django import views
from django.shortcuts import redirect, render
from shop.forms import SignupForm

from shop.models.myuser import MyUser
from uuid import uuid4

from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

def send_user_mail(email,token,request):
    current_site=get_current_site(request)
    subject="Account verification Mail"
    message=f'Please Verify your email {current_site}/account_verify/{token}'
    
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[email]

    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)


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
            send_user_mail(email=createuser.email,token=createuser.token,request=request)

            return render(request,'index.html')
        data['error']=error
        data['first_name']=First_Name
        print(error)
        return render(request,"signup.html",data)
        

def email_verify_by_link(request,token):

    user= MyUser.objects.get(token=token)

    if not user:
        error="Please clink the valid link  "
    else:
        
        user.email_verify=True
        user.save()

    print(token)
    return redirect("signup")




