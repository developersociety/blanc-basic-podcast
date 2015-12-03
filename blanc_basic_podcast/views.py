from django.views.generic import ListView, DateDetailView
from django.utils import timezone
from django.conf import settings
from . import get_podcastfile_model


class PodcastFileListView(ListView):
    model = get_podcastfile_model()
    paginate_by = getattr(settings, 'PODCAST_PER_PAGE', 10)

    def get_queryset(self):
        qs = super(PodcastFileListView, self).get_queryset()
        return qs.filter(published=True, date__lte=timezone.now())


class PodcastFileDetailView(DateDetailView):
    queryset = get_podcastfile_model().objects.filter(published=True)
    month_format = '%m'
    date_field = 'date'
