# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import blanc_basic_podcast.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PodcastFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(max_length=100, unique_for_date='date')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('file', models.FileField(help_text='MP3/MP4 files only', upload_to='podcast/file/%Y/%m', validators=[blanc_basic_podcast.validators.validate_mpeg_file])),
                ('description', models.TextField()),
                ('published', models.BooleanField(default=True, help_text='File will be hidden unless this option is selected', db_index=True)),
                ('duration', models.PositiveIntegerField(default=0, editable=False)),
            ],
            options={
                'ordering': ('-date',),
                'get_latest_by': 'date',
            },
            bases=(models.Model,),
        ),
    ]
