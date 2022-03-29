from django import views
from django.shortcuts import render
from django.views import View
# Create your views here.

class Index(views.View):

    def get(self,request):
        return render(request,'index.html')