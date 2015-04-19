# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodsmenu', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Description',
            field=models.TextField(null=True, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
            preserve_default=True,
        ),
    ]
