# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-08 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servers', '0006_auto_20171025_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameters',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
    ]
