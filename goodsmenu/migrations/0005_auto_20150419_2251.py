# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodsmenu', '0004_product_title_english'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Photo',
            field=models.ImageField(upload_to=b'/media/uploads/articleimages/', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe'),
            preserve_default=True,
        ),
    ]
