from django.conf import settings
from django.utils import timezone
from django.views.generic import DateDetailView, ListView

from .models import PodcastFile


class PodcastFileListView(ListView):
    model = PodcastFile
    paginate_by = getattr(settings, 'PODCAST_PER_PAGE', 10)

    def get_queryset(self):
        qs = super(PodcastFileListView, self).get_queryset()
        return qs.filter(published=True, date__lte=timezone.now())


class PodcastFileDetailView(DateDetailView):
    queryset = PodcastFile.objects.filter(published=True)
    month_format = '%m'
    date_field = 'date'
