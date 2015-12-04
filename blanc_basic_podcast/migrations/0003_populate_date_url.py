# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def populate_date_url(apps, schema_editor):
    PodcastFile = apps.get_model('podcast', 'PodcastFile')

    for obj in PodcastFile.objects.all():
        obj.date_url = obj.date.date()
        obj.save()


def remove_date_url(apps, schema_editor):
    PodcastFile = apps.get_model('podcast', 'PodcastFile')
    PodcastFile.objects.update(date_url=None)


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0002_podcastfile_date_url'),
    ]

    operations = [
        migrations.RunPython(populate_date_url, remove_date_url),
    ]
