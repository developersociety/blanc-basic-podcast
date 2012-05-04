from django.conf.urls import patterns, url
import feeds
import views


urlpatterns = patterns('',
    # RSS feed
    url(r'^feed/',
        feeds.BasicPodcastFeed(),
        name='feed'),

    # Pages
    url(r'^$',
        views.PodcastFileListView.as_view(),
        name='file-list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        views.PodcastFileDetailView.as_view(),
        name='file-detail'),
)
