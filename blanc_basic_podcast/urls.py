from django.conf import settings
from django.conf.urls import url

from . import feeds, views


# RSS feed - always enabled
urlpatterns = [
    url(r'^feed/$',
        feeds.BasicPodcastFeed(),
        name='feed'),
]

# Pages
page_patterns = [
    url(r'^$',
        views.PodcastFileListView.as_view(),
        name='file-list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        views.PodcastFileDetailView.as_view(),
        name='file-detail'),
]

# Setting PODCAST_PAGES to False in settings.py will disable pages.
if getattr(settings, 'PODCAST_PAGES', True):
    urlpatterns += page_patterns
