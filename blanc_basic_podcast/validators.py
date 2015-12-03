from django.core.exceptions import ValidationError
from hsaudiotag import auto
from hsaudiotag.mpeg import Mpeg
from hsaudiotag.mp4 import File as Mp4File


def validate_mpeg_file(mpeg_file):
    audio_file = auto.File(mpeg_file.file)
    file_type = audio_file.original

    # Only allow MP3/MP4 files
    if file_type is None or not isinstance(file_type, (Mpeg, Mp4File)):
        raise ValidationError(u'Not a valid MP3/MP4 file')

    # Don't want empty files
    if audio_file.duration == 0:
        raise ValidationError(u"Audio file has no duration (file may be empty)")
