# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-23 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('sname', models.CharField(max_length=20)),
                ('sloc', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images')),
                ('profile', models.FileField(upload_to='files')),
            ],
        ),
    ]
