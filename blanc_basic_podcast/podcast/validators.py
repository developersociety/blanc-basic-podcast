from django.core.exceptions import ValidationError
from hsaudiotag import auto
from hsaudiotag.mpeg import Mpeg


def validate_mp3(mp3_file):
    audio_file = auto.File(mp3_file.file)
    file_type = audio_file.original

    # Currently only allow MP3 files
    if file_type is None or not isinstance(file_type, Mpeg):
        raise ValidationError(u'Not a valid MP3 file')

    # Don't want empty files
    if audio_file.duration == 0:
        raise ValidationError(u"MP3 has no duration (file may be empty)")
