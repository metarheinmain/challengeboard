# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20150818_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='datetime_end',
            field=models.DateTimeField(blank=True, verbose_name='End date', null=True),
        ),
    ]
