# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-07 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyrecord',
            name='score',
            field=models.IntegerField(choices=[(100, b'A+'), (90, b'A'), (85, b'B+'), (80, b'B'), (70, b'B-'), (60, b'C+'), (50, b'C'), (40, b'C-'), (0, b'D'), (b'-1', b'N/A'), (-100, b'COPY'), (-1000, b'FAIL')], default=b'-1', verbose_name='\u672c\u8282\u6210\u7ee9'),
        ),
    ]
