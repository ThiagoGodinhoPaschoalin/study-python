from pytubefix import YouTube, Stream, StreamQuery
from pytubefix.cli import on_progress

def converter_segundos(tempo_em_segundos): 
  minutos, segundos = divmod(tempo_em_segundos, 60) 
  return f"{minutos}:{segundos:02}"

def download_media(youtube_url, media_type="video"):
  yt = YouTube(youtube_url)
  stream: Stream = None

  warn: str = ''

  if media_type == "video":
    stream = yt.streams.get_highest_resolution()
    stream = yt.streams.filter(res=stream.resolution, progressive=True).first()

    if stream.filesize_kb >= 9216.0:
      warn = f"O vídeo possui {stream.filesize_kb} KB, porém o máximo permitido é de 9216.0 KB.\nQuando esse valor é ultrapassado, o vídeo fica cortado.\nPor esse motivo, o download foi alterado para ÁUDIO."
      media_type = "audio"

  if media_type == "audio":
    stream = None
    stream = yt.streams.filter(only_audio=True).first()
  
  file = stream.download()

  return { "file": file, "warn": warn }

def get_video_info(youtube_url):
  yt = YouTube(youtube_url)
  video = yt.streams.get_highest_resolution()
  audio = yt.streams.get_audio_only()
  return {
    "title": yt.title,
    "author": yt.author,
    "duration": converter_segundos(yt.length),
    "video": { 'limit': '9_216.0 KB', 'filesize_kb': video.filesize_kb, 'resolution': video.resolution, 'can_download': video.filesize_kb < 9216.0 },
    "audio": { 'limit': '24_448.6 KB', 'filesize_kb': audio.filesize_kb, 'average_bitrate': audio.abr, 'can_download': audio.filesize_kb < 24448.6 }
  }

