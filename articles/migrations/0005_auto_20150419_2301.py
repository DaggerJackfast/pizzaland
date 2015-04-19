# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20150419_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='Photo',
            field=models.ImageField(upload_to=b'media/uploads/articleimages/', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe', blank=True),
            preserve_default=True,
        ),
    ]
