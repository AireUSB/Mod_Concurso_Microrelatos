# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concurso', '0004_auto_20150408_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweetcargado',
            name='rating',
        ),
        migrations.AddField(
            model_name='tweetcargado',
            name='juez1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tweetcargado',
            name='juez2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tweetcargado',
            name='juez3',
            field=models.IntegerField(default=0),
        ),
    ]
