# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concurso', '0002_auto_20150408_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetcargado',
            name='idRef',
            field=models.BigIntegerField(),
        ),
    ]
