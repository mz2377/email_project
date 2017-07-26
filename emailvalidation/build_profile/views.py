# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import User
from .forms import RegisterForm
from django.urls import reverse
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

# Create your views here.

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			#save the receiver email address
			to_email = form.cleaned_data.get('email_acct')
			#generate emcryption code and validation_url to be sent to email
			encryption_code = get_random_string(length=32)
			encrypted_validation_url = '%s%s/' % (request.META.get('HTTP_REFERER'),encryption_code)
			print encrypted_validation_url
			#save our new registered user into our User database schema
			form.save(commit=True)
			#send email from default gmail acct in settings.py to to_email with encryption code
			send_mail('Validation Email', 'Please go to this url link to confirm registering your email account: %s' % encrypted_validation_url,
				'evergreenz1995@gmail.com',[to_email])
			#display a thanks and email sent message on page
			return HttpResponseRedirect('thanks/')
	else: #request.method == 'GET'
		form = RegisterForm()
	return render(request, 'profile/register.html', {'form':form})

def register_thanks(request):
	return HttpResponse("We've sent you a validation email.")

def validate(request,decryption_code):
	#print decryption_code
	#find way to update code in model and change is_validated from false to true
	return HttpResponse("success!")