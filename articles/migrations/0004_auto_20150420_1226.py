# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20150420_1222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='Description',
            new_name='Text',
        ),
    ]
