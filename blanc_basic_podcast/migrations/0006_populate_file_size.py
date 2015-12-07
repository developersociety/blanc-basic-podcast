# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def populate_file_size(apps, schema_editor):
    PodcastFile = apps.get_model('podcast', 'PodcastFile')

    for obj in PodcastFile.objects.all():
        obj.file_size = obj.file.size
        obj.save()


def remove_file_size(apps, schema_editor):
    PodcastFile = apps.get_model('podcast', 'PodcastFile')
    PodcastFile.objects.update(file_size=0)


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0005_podcastfile_file_size'),
    ]

    operations = [
        migrations.RunPython(populate_file_size, remove_file_size),
    ]
