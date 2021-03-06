# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-24 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servers', '0002_FirstCustomTemplateServer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='help text')),
                ('category', models.IntegerField(choices=[(1, 'Global Variables'), (2, 'Local Network Connection'), (3, 'Jenkins Connection')], default=1, verbose_name='category')),
            ],
            options={
                'verbose_name': 'parameter',
                'verbose_name_plural': 'parameters',
                'db_table': 'parameters',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='serverprofile',
            name='category',
            field=models.IntegerField(choices=[(1, 'Global Variables'), (2, 'Local Network Connection'), (3, 'Jenkins Connection')], default=1, verbose_name='category'),
        ),
        migrations.AddField(
            model_name='templateserver',
            name='category',
            field=models.IntegerField(choices=[(1, 'Global Variables'), (2, 'Local Network Connection'), (3, 'Jenkins Connection')], default=1, verbose_name='category'),
        ),
        migrations.RemoveField(
            model_name='templateserver',
            name='parameters',
        ),
        migrations.AddField(
            model_name='templateserver',
            name='parameters',
            field=models.ManyToManyField(blank=True, to='Servers.Parameters'),
        ),
    ]
