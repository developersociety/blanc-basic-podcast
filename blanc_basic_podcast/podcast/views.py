from django.views.generic import ListView, DateDetailView
from django.utils import timezone
from django.conf import settings
from .models import PodcastFile


class PodcastFileListView(ListView):
    paginate_by = getattr(settings, 'PODCAST_PER_PAGE', 10)

    def get_queryset(self):
        return PodcastFile.objects.filter(published=True,
                date__lte=timezone.now())


class PodcastFileDetailView(DateDetailView):
    queryset = PodcastFile.objects.filter(published=True)
    month_format = '%m'
    date_field = 'date'
