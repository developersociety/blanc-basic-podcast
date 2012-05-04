from hsaudiotag import auto


def file_duration(mp3_file):
    audio_file = auto.File(mp3_file.file)
    return audio_file.duration
