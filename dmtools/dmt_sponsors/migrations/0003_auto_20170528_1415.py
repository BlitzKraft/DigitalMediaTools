# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-28 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmt_sponsors', '0002_auto_20170528_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='dmt_feature',
            field=models.CharField(choices=[('1', 'Yes'), ('0', 'No')], max_length=1, verbose_name='Feature'),
        ),
    ]
