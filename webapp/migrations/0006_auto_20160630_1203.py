# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-30 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20160503_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cultivo',
            name='inicialesH20',
        ),
        migrations.RemoveField(
            model_name='cultivo',
            name='inicialesNO3',
        ),
        migrations.RemoveField(
            model_name='cultivo',
            name='suelos',
        ),
        migrations.RemoveField(
            model_name='cultivo',
            name='tipocultivares',
        ),
        migrations.AddField(
            model_name='inicialh20',
            name='suelo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.Cultivo'),
            preserve_default=False,
        ),
    ]
