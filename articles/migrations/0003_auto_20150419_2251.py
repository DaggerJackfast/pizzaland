# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20150419_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='Author',
            field=models.CharField(max_length=50, verbose_name=b'\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articles',
            name='Date',
            field=models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articles',
            name='Photo',
            field=models.ImageField(upload_to=b'/media/uploads/articleimages/', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe', blank=True),
            preserve_default=True,
        ),
    ]
