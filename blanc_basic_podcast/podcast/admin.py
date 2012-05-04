from django.contrib import admin
from django.contrib.sites.models import Site
from .models import PodcastFile


admin.site.register(PodcastFile)
