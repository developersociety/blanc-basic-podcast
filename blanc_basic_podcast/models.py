from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from .utils import file_duration
from .validators import validate_mpeg_file


class PodcastFile(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique_for_date='date')
    date = models.DateTimeField(default=timezone.now, db_index=True)
    date_url = models.DateField(db_index=True, editable=False)
    file = models.FileField(
        upload_to='podcast/file/%Y/%m', validators=[validate_mpeg_file],
        help_text='MP3/MP4 files only')
    description = models.TextField()
    published = models.BooleanField(
        default=True, db_index=True, help_text='File will be hidden unless this option is selected')
    duration = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        get_latest_by = 'date'
        ordering = ('-date',)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.date_url = self.date.date()
        self.duration = file_duration(self.file)
        super(PodcastFile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        if getattr(settings, 'PODCAST_PAGES', True):
            return reverse('blanc_basic_podcast:file-detail', kwargs={
                'year': self.date_url.year,
                'month': str(self.date_url.month).zfill(2),
                'day': str(self.date_url.day).zfill(2),
                'slug': self.slug,
            })
        else:
            return self.file.url

    @property
    def time_duration(self):
        hours = self.duration / 3600
        remaining = self.duration % 3600

        minutes = remaining / 60
        seconds = remaining % 60

        return '%d:%02d:%02d' % (hours, minutes, seconds)