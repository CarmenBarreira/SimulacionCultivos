# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-01 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_riego'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultivo',
            name='value',
            field=models.CharField(default='MZ', max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]