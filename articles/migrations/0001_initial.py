# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=250, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('Text', models.TextField(null=True, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82', blank=True)),
                ('Author', models.CharField(max_length=50, verbose_name=b'\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80')),
                ('Date', models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('Photo', models.ImageField(default=b'uploads/articleImages/default_image.png', upload_to=b'uploads/articleImages', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe', blank=True)),
            ],
            options={
                'db_table': 'articles',
                'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u044f',
                'verbose_name_plural': '\u0441\u0442\u0430\u0442\u044c\u0438',
            },
            bases=(models.Model,),
        ),
    ]
