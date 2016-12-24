# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qualification', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pathway',
            old_name='pathway',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='qualification',
            name='framework',
            field=models.CharField(choices=[('QCF', 'QCF (Qualifications and Credit Framework)'), ('NQF', 'NQF (National Qualification Framework)')], default='QCF', max_length=3),
        ),
    ]
