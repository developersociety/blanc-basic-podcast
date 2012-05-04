from django.views.generic import ListView, DateDetailView
from .models import PodcastFile


class PodcastFileListView(ListView):
    queryset = PodcastFile.objects.filter(published=True)


class PodcastFileDetailView(DateDetailView):
    queryset = PodcastFile.objects.filter(published=True)
    month_format = '%m'
    date_field = 'date'
