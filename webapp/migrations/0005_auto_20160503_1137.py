# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 14:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20160502_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cultivo',
            name='fechasiembra',
        ),
        migrations.RemoveField(
            model_name='cultivo',
            name='inicialesH20',
        ),
        migrations.AddField(
            model_name='cultivo',
            name='inicialesH20',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.InicialH20'),
            preserve_default=False,
        ),
    ]
