#Add URL maps to redirect the base URL to our application Build_Profile
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from . import views

urlpatterns = [
	#/register/
    url(r'^register/$', views.register,name='register'),
    #/register/validate_email
    url(r'^register/validate_email/(?P<token>(.*))/$', views.validate, name='validate_email'),


]

