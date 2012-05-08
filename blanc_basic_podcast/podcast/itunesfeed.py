from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed


class iTunesFeed(Rss201rev2Feed):
    def rss_attributes(self):
        attrs = super(iTunesFeed, self).rss_attributes()
        attrs['xmlns:itunes'] = 'http://www.itunes.com/dtds/podcast-1.0.dtd'
        return attrs

    def add_root_elements(self, handler):
        super(iTunesFeed, self).add_root_elements(handler)

        # Add owner details as iTunes fields
        if (self.feed['author_email'] is not None
                or self.feed['author_name'] is not None):
            handler.startElement(u'itunes:owner', {})

            if self.feed['author_email'] is not None:
                handler.addQuickElement(
                        u'itunes:email', self.feed['author_email'])

            if self.feed['author_name'] is not None:
                handler.addQuickElement(
                        u'itunes:name', self.feed['author_name'])

            handler.endElement(u'itunes:owner')

        # iTunes explicit
        if self.feed['itunes:explicit'] is not None:
            handler.addQuickElement(
                    u'itunes:explicit', self.feed['itunes:explicit'])

        # iTunes explicit
        if self.feed['itunes:image'] is not None:
            handler.addQuickElement(u'itunes:image', '', {
                'href': self.feed['itunes:image'],
            })

        # iTunes Categories
        if self.feed['itunes:categories'] is not None:
            for i in self.feed['itunes:categories']:
                if isinstance(i, basestring):
                    # Single category
                    handler.addQuickElement(u'itunes:category', '', {
                        'text': i,
                    })
                else:
                    # Category with sub-category
                    for j in i:
                        handler.startElement(u'itunes:category', {
                            'text': j,
                        })
                    for j in i:
                        handler.endElement(u'itunes:category')

    def add_item_elements(self, handler, item):
        super(iTunesFeed, self).add_item_elements(handler, item)

        # File length in hours/mins/seconds
        if item['itunes:duration']:
            handler.addQuickElement(
                    u'itunes:duration', item['itunes:duration'])


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
            'itunes:image': self.itunes_image,
        }
