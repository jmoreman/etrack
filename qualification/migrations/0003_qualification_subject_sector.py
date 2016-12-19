# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 19:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0001_initial'),
        ('qualification', '0002_auto_20161218_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualification',
            name='subject_sector',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='misc.SubjectSector'),
            preserve_default=False,
        ),
    ]
