from django.conf.urls import patterns, url
from django.conf import settings
import feeds
import views


# RSS feed
feed_patterns = patterns('',
    url(r'^feed/$',
        feeds.BasicPodcastFeed(),
        name='feed'),
)

# Pages
page_patterns = patterns('',
    url(r'^$',
        views.PodcastFileListView.as_view(),
        name='file-list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        views.PodcastFileDetailView.as_view(),
        name='file-detail'),
)

# Build the final URL patterns, setting PODCAST_PAGES to False in settings.py
# will disable pages.
urlpatterns = feed_patterns

if getattr(settings, 'PODCAST_PAGES', True):
    urlpatterns += page_patterns
