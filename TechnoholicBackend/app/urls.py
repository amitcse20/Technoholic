from django.urls import path
from .views import *


urlpatterns=[
    path('',index,name='index'),
    path('login',login,name='login'),
    path('signup',signup,name='signup'),
    path('course',course,name='course'),
    path('links',links,name='links')
]
