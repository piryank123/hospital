# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-19 11:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_auto_20160518_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 19, 11, 4, 52, 291644, tzinfo=utc), verbose_name='datetime'),
            preserve_default=False,
        ),
    ]
