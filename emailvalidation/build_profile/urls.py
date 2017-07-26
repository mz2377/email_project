#Add URL maps to redirect the base URL to our application Build_Profile
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from . import views

urlpatterns = [
	#/register/
    url(r'^register/$', views.register,name='register'),
    #/register/thanks/
    url(r'^register/thanks/$', views.register_thanks,name='thanks'),
    #/register/####_DECRYPTION_CODE
    url(r'^register/(?P<decryption_code>[\w{}.-]{32})/$', views.validate, name='validate_email'),

]

