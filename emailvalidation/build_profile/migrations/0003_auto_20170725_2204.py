# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 22:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('build_profile', '0002_auto_20170725_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailacct',
            name='user_id',
        ),
        migrations.AddField(
            model_name='user',
            name='email_acct',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='build_profile.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='validation_code',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='EmailAcct',
        ),
    ]