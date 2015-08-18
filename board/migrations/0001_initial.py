# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
                ('location', models.CharField(max_length=300, blank=True, null=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('mode', models.CharField(max_length=100, choices=[('max', 'Highest value wins'), ('min', 'Lowest value wins'), ('first', 'First entry wins')])),
                ('value_unit', models.CharField(max_length=300, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('value', models.FloatField(blank=True, null=True)),
                ('datetime', models.DateTimeField()),
                ('challenge', models.ForeignKey(to='board.Challenge')),
            ],
        ),
    ]
