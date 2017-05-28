# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-28 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmt_sponsors', '0003_auto_20170528_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='dmt_email',
            field=models.CharField(max_length=250, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='dmt_name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='dmt_password',
            field=models.CharField(max_length=25, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='dmt_url',
            field=models.CharField(max_length=250, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='dmt_user',
            field=models.CharField(max_length=25, verbose_name='Username'),
        ),
    ]