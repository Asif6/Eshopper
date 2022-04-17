from django.urls import path

from .views.index import Index
from .views.signup import Signup
from .views.login import Login
from .views.signup import email_verify_by_link

urlpatterns=[
    path("",Index.as_view(),name='index'),
    path("signup/",Signup.as_view(),name='signup'),
    path("login/",Login.as_view(),name='login'),
    path("account_verify/<slug:token>",email_verify_by_link,name="email_verify")
]