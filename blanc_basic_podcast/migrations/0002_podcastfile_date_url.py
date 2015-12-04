# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcastfile',
            name='date_url',
            field=models.DateField(null=True, editable=False, db_index=True),
            preserve_default=True,
        ),
    ]
