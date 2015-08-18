# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='challenge',
            field=models.ForeignKey(related_name='participants', to='board.Challenge'),
        ),
    ]
