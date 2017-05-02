# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 12:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0003_auto_20170427_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField(default=datetime.date.today)),
                ('scheme', models.CharField(max_length=250)),
                ('path', models.CharField(max_length=250)),
                ('method', models.CharField(max_length=250)),
                ('content_type', models.CharField(max_length=250)),
            ],
        ),
    ]
