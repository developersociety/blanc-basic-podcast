from django.core.exceptions import ImproperlyConfigured


def get_podcastfile_model():
    from django.conf import settings
    from django.db.models import get_model

    post_model = getattr(settings, 'PODCAST_FILE_MODEL', 'podcast.PodcastFile')

    try:
        app_label, model_name = post_model.split('.')
    except ValueError:
        raise ImproperlyConfigured("PODCAST_FILE_MODEL must be of the form 'app_label.model_name'")
    obj_model = get_model(app_label, model_name)
    if obj_model is None:
        raise ImproperlyConfigured("PODCAST_FILE_MODEL refers to model '%s' that has not been installed" % obj_model)
    return obj_model
