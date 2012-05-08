from django.db import models
from django.utils import timezone
from .validators import validate_mp3
from .utils import file_duration


class PodcastFile(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique_for_date='date')
    date = models.DateTimeField(default=timezone.now, db_index=True)
    file = models.FileField(
            upload_to='podcast/file/%Y/%m',
            validators=[validate_mp3],
            help_text='MP3 files only')
    description = models.TextField()
    published = models.BooleanField(
            default=True,
            db_index=True,
            help_text='File will be hidden unless this option is selected')
    duration = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        get_latest_by = 'date'
        ordering = ('-date',)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.duration = file_duration(self.file)
        super(PodcastFile, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('blanc_basic_podcast:file-detail', (), {
            'year': self.date.year,
            'month': str(self.date.month).zfill(2),
            'day': str(self.date.day).zfill(2),
            'slug': self.slug,
        })

    @property
    def time_duration(self):
        hours = self.duration / 3600
        remaining = self.duration % 3600

        minutes = remaining / 60
        seconds = remaining % 60

        return '%d:%02d:%02d' % (hours, minutes, seconds)
