# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tweetCargado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idRef', models.IntegerField()),
                ('rtCount', models.IntegerField()),
                ('text', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
