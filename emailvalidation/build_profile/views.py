# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import User, Email
from .forms import RegisterForm
from django.urls import reverse
from django.core.mail import send_mail
from django.core import signing
from django.http import JsonResponse

# Create your views here.

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			#save/update user
			form.save()
			to_email = form.cleaned_data.get('email_acct')
			user_i = User.objects.get(email_acct=to_email)
			#encrypt the new user info
			auth_key = signing.dumps(to_email)
			user_i.email_set.create(email_acct=to_email,validation_key = auth_key)
			user_i.save()
			#send email from default gmail acct in settings.py to to_email with encryption code
			unsigned_validation_url = '%svalidate_email/' % request.META.get('HTTP_REFERER')
			signed_validation_url = unsigned_validation_url+str(auth_key)
			send_mail('Validation Email', 'Please go to this url link to confirm registering your email account: %s' % signed_validation_url,
				'evergreenz1995@gmail.com',[to_email])
			return HttpResponse("Thank you for registering. A verification link was sent to your email.")
	else: #request.method == 'GET'
		form = RegisterForm()
	return render(request, 'profile/register.html', {'form':form})


def validate(request,token):
	try:
		new_verified_email = Email.objects.get(validation_key=token)
		new_verified_email.email_is_validated = True
		new_verified_email.save()
	except:
		return Http404("No registered email associated with this URL token!")
	return HttpResponse("Thank you for verifying your email account.")
