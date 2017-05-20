# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='wowclass',
            field=models.CharField(max_length=3, default='', choices=[('DK', 'Death Knight'), ('DH', 'Demon Hunter'), ('MON', 'Monk'), ('SHA', 'Shaman'), ('PAL', 'Paladin')]),
        ),
    ]
