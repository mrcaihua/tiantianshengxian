# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttsx_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='ucode',
            field=models.CharField(default=b'', max_length=6),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='ushow',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uaddrss',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uphone',
            field=models.CharField(default=b'', max_length=11),
        ),
    ]
