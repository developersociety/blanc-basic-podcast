from django.contrib import admin
from .models import PodcastFile


class PodcastFileAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'date', 'file', 'description')
        }),
        ('Advanced options', {
            'fields': ('slug', 'published')
        }),
    )
    date_hierarchy = 'date'
    list_display = ('title', 'date', 'published')
    list_editable = ('published',)
    list_filter = ('published', 'date')
    search_fields = ('title',)
    prepopulated_fields = {
        'slug': ('title',)
    }


admin.site.register(PodcastFile, PodcastFileAdmin)
