# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goodsmenu', '0003_auto_20150416_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Title_English',
            field=models.CharField(default=datetime.datetime(2015, 4, 19, 15, 44, 45, 611000, tzinfo=utc), max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\xd0\x9f\xd0\xbe\xd0\x90\xd0\xbd\xd0\xb3\xd0\xbb\xd0\xb8\xd0\xb9\xd1\x81\xd0\xba\xd0\xb8'),
            preserve_default=False,
        ),
    ]
