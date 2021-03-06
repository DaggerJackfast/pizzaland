# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=50, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('Description', models.TextField(null=True, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'db_table': 'category',
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('Title_English', models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\xd0\x9f\xd0\xbe\xd0\x90\xd0\xbd\xd0\xb3\xd0\xbb\xd0\xb8\xd0\xb9\xd1\x81\xd0\xba\xd0\xb8')),
                ('Price', models.DecimalField(default=0.0, verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0', max_digits=12, decimal_places=2)),
                ('Description', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('Discount', models.FloatField(default=0.0, verbose_name=b'\xd0\xa1\xd0\xba\xd0\xb8\xd0\xb4\xd0\xba\xd0\xb0')),
                ('Status', models.BooleanField(default=False, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81')),
                ('Photo', models.ImageField(default=b'uploads/productsImages/default_image.png', upload_to=b'uploads/productImages', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe')),
                ('Weight', models.FloatField(default=0.0, verbose_name=b'\xd0\x92\xd0\xb5\xd1\x81')),
                ('Diameter', models.FloatField(default=0.0, verbose_name=b'\xd0\x94\xd0\xb8\xd0\xb0\xd0\xbc\xd0\xb5\xd1\x82\xd1\x80')),
                ('Ingredients', models.TextField(verbose_name=b'\xd0\x98\xd0\xbd\xd0\xb3\xd1\x80\xd0\xb8\xd0\xb4\xd0\xb8\xd0\xb5\xd0\xbd\xd1\x82\xd1\x8b', blank=True)),
                ('ProductCategory', models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', to='goodsmenu.Category')),
            ],
            options={
                'db_table': 'product',
                'verbose_name': '\u0422\u043e\u0432\u0430\u0440',
                'verbose_name_plural': '\u0442\u043e\u0432\u0430\u0440\u044b',
            },
            bases=(models.Model,),
        ),
    ]
