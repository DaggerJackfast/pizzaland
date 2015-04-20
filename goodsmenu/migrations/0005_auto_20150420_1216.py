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
            name='Description',
            field=models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='Diameter',
            field=models.FloatField(default=0.0, verbose_name=b'\xd0\x94\xd0\xb8\xd0\xb0\xd0\xbc\xd0\xb5\xd1\x82\xd1\x80'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='Ingredients',
            field=models.TextField(verbose_name=b'\xd0\x98\xd0\xbd\xd0\xb3\xd1\x80\xd0\xb8\xd0\xb4\xd0\xb8\xd0\xb5\xd0\xbd\xd1\x82\xd1\x8b', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='Photo',
            field=models.ImageField(default=b'uploads/productsImages/default_image.png', upload_to=b'uploads/productImages', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='Price',
            field=models.DecimalField(default=0.0, verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0', max_digits=12, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='Weight',
            field=models.FloatField(default=0.0, verbose_name=b'\xd0\x92\xd0\xb5\xd1\x81'),
            preserve_default=True,
        ),
    ]
