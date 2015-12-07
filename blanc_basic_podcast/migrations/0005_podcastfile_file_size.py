# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0004_date_url_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcastfile',
            name='file_size',
            field=models.PositiveIntegerField(editable=False, default=0),
            preserve_default=True,
        ),
    ]
