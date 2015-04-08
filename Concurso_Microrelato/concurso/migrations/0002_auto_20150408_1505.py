# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concurso', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetcargado',
            name='estado',
            field=models.CharField(default=b'P', max_length=1, choices=[(b'A', b'Aprobado'), (b'R', b'Rechazado'), (b'P', b'Pendiente')]),
        ),
        migrations.AddField(
            model_name='tweetcargado',
            name='userRef',
            field=models.CharField(default=b'', max_length=40),
        ),
    ]
