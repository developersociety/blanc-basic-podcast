from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.contrib.sites.models import Site
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils import timezone
import mimetypes
from .itunesfeed import PodcastFeed
from .models import PodcastFile


class BasicPodcastFeed(PodcastFeed):
    title = getattr(settings, 'PODCAST_TITLE', 'Podcast')
    link = reverse_lazy('blanc_basic_podcast:file-list')

    author_name = settings.PODCAST_AUTHOR
    author_email = settings.PODCAST_EMAIL

    itunes_explicit = getattr(settings, 'PODCAST_EXPLICIT', 'no')
    itunes_categories = settings.PODCAST_CATEGORIES

    @property
    def itunes_image(self):
        file_url = staticfiles_storage.url(settings.PODCAST_IMAGE)

        # Must be a full URL
        if not (file_url.startswith('http://')
                or file_url.startswith('https://')):
            domain = Site.objects.get_current().domain
            file_url = 'http://%s%s' % (domain, file_url)

        return file_url

    def items(self):
        feed_limit = getattr(settings, 'PODCAST_FEED_LIMIT', 10)
        return PodcastFile.objects.filter(published=True,
                date__lte=timezone.now())[:feed_limit]

    def item_description(self, obj):
        return obj.description

    def item_pubdate(self, obj):
        return obj.date

    def item_guid(self, obj):
        return u'%s:podcast:%d' % (Site.objects.get_current().domain, obj.pk)

    def item_enclosure_url(self, obj):
        file_url = obj.file.url

        # Must be a full URL
        if not (file_url.startswith('http://')
                or file_url.startswith('https://')):
            domain = Site.objects.get_current().domain
            file_url = 'http://%s%s' % (domain, file_url)

        return file_url

    def item_enclosure_mime_type(self, obj):
        return mimetypes.guess_type(obj.file.path)[0]

    def item_enclosure_length(self, obj):
        return obj.file.size

    def item_itunes_duration(self, obj):
        return obj.time_duration
