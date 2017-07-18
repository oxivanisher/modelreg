# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import modelreg.models


class Migration(migrations.Migration):

    dependencies = [
        ('modelreg', '0005_auto_20170514_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='identifier',
            field=models.CharField(blank=True, default=modelreg.models.make_identifier, max_length=10),
        ),
        migrations.AlterField(
            model_name='publicprofile',
            name='auth',
            field=models.CharField(blank=True, default=modelreg.models.make_identifier, max_length=10),
        ),
        migrations.AlterField(
            model_name='publicprofile',
            name='identifier',
            field=models.CharField(blank=True, default=modelreg.models.make_identifier, max_length=10),
        ),
    ]
