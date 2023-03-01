from django.core.files import File
from pydub import AudioSegment
from pathlib import Path
import os


def convert_to_mp3(audio_file, target_filetype='mp3', content_type='audio/mpeg',bitrate="192k"):

    file_path = audio_file.temporary_file_path()
    original_extension = file_path.split('.')[-1]
    mp3_converted_file = AudioSegment.from_file(file_path, original_extension)

    new_path = file_path[:-3] + target_filetype
    mp3_converted_file.export(new_path, format=target_filetype, bitrate="192k")

    converted_audiofile = File(
                file=open(new_path, 'rb'),
                name=Path(new_path)
            )
    converted_audiofile.name = Path(new_path).name
    converted_audiofile.content_type = content_type
    converted_audiofile.size = os.path.getsize(new_path)
    return converted_audiofile