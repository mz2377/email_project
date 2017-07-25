# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


# Create your models here.

class User(models.Model):
	"""Personal info parameters are first, last, username, join_date, email_accts """
	first = models.CharField(max_length=200,null=True)
	last = models.CharField(max_length=200,null=True)
	join_date = models.DateField(auto_now_add=True)
	user_id = models.ForeignKey('User', null=True, on_delete=models.CASCADE)
	username = models.CharField(max_length=200,null=True)
	email_acct = models.CharField(max_length=1000,null=True)
	password = models.CharField(max_length=100,null=True)
	validation_code = models.IntegerField(null=True)
	is_validated = models.BooleanField(default=False)
	def __str__(self):
		return self.username





    
