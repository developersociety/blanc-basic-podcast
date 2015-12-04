from __future__ import unicode_literals

from django.contrib.syndication.views import Feed
from django.utils import six
from django.utils.feedgenerator import Rss201rev2Feed


class iTunesFeed(Rss201rev2Feed):
    def rss_attributes(self):
        attrs = super(iTunesFeed, self).rss_attributes()
        attrs['xmlns:itunes'] = 'http://www.itunes.com/dtds/podcast-1.0.dtd'
        return attrs

    def add_root_elements(self, handler):
        super(iTunesFeed, self).add_root_elements(handler)

        # Add owner details as iTunes fields
        if (self.feed['author_email'] is not None or self.feed['author_name'] is not None):
            handler.startElement('itunes:owner', {})

            if self.feed['author_email'] is not None:
                handler.addQuickElement('itunes:email', self.feed['author_email'])

            if self.feed['author_name'] is not None:
                handler.addQuickElement('itunes:name', self.feed['author_name'])

            handler.endElement('itunes:owner')

        # Need an iTunes author as well
        if self.feed['author_name'] is not None:
            handler.addQuickElement('itunes:author', self.feed['author_name'])

        # iTunes explicit
        if self.feed['itunes:explicit'] is not None:
            handler.addQuickElement('itunes:explicit', self.feed['itunes:explicit'])

        # iTunes image
        if self.feed['itunes:image'] is not None:
            handler.addQuickElement('itunes:image', '', {
                'href': self.feed['itunes:image'],
            })

        # iTunes description/summary
        if self.feed['itunes:summary'] is not None:
            handler.addQuickElement('itunes:summary', self.feed['itunes:summary'])

        # iTunes Categories
        if self.feed['itunes:categories'] is not None:
            for category in self.feed['itunes:categories']:
                if isinstance(category, six.text_type):
                    # Single category
                    handler.addQuickElement('itunes:category', '', {
                        'text': category,
                    })
                else:
                    # Category with sub-category
                    for subcategory in category:
                        handler.startElement('itunes:category', {
                            'text': subcategory,
                        })
                    for subcategory in category:
                        handler.endElement('itunes:category')

    def add_item_elements(self, handler, item):
        super(iTunesFeed, self).add_item_elements(handler, item)

        # File length in hours/mins/seconds
        if item['itunes:duration']:
            handler.addQuickElement('itunes:duration', item['itunes:duration'])


class PodcastFeed(Feed):
    feed_type = iTunesFeed

    def item_extra_kwargs(self, item):
        return {
            'itunes:duration': self.item_itunes_duration(item),
        }

    def feed_extra_kwargs(self, obj):
        return {
            'itunes:explicit': self.itunes_explicit,
            'itunes:categories': self.itunes_categories,
            'itunes:summary': self.itunes_summary,
            'itunes:image': self.itunes_image,
        }
