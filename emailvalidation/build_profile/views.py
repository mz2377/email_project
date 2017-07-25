# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import User
from .forms import RegisterForm
from django.urls import reverse
from django.core.mail import send_mail
# Create your views here.

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return HttpResponseRedirect('thanks/')
	else: #request.method == 'GET'
		form = RegisterForm()
	return render(request, 'profile/register.html', {'form':form})

def register_thanks(request):
	send_mail('Validation Email','Please click this link to confirm registering your email account:',
		'mz2377@columbia.edu', ['ming.zhao@humandx.org'])

	return HttpResponse("We've sent you a validation email.")

def validate(request,encrypted_code):
	try:
		new_valid_email = EmailAcct.objects.get(validation_code=encrypted_code)
		new_valid_email.is_validated = True
	except EmailAcct.DoesNotExist:
		raise Http404("No account associated with this email yet!")
	return render(request,'profile/validate.html',{new_valid_email})