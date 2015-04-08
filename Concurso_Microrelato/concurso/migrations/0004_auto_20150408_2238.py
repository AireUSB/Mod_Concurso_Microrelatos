# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concurso', '0003_auto_20150408_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweetcargado',
            name='id',
        ),
        migrations.AlterField(
            model_name='tweetcargado',
            name='idRef',
            field=models.BigIntegerField(serialize=False, primary_key=True),
        ),
    ]
