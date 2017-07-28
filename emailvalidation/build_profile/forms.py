from django import forms
from django.db import models
from .models import User
import datetime
from django.utils.crypto import get_random_string


class RegisterForm(forms.ModelForm):
	first = forms.CharField(label='First name',max_length=200)
	last = forms.CharField(label='Last name',max_length=200)
	username = forms.CharField(label='Username',max_length=200)
	email_acct = forms.EmailField(label='Email',max_length=1000)
	password = forms.CharField(label='Password',max_length=100)

	class Meta:
		model = User
		fields = ('first','last','username','email_acct','password')


