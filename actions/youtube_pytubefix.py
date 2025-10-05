from pytubefix import YouTube, Stream
from pytubefix.cli import on_progress

# https://github.com/JuanBindez/pytubefix
# https://pytubefix.readthedocs.io/en/latest
# pip install pytubefix

def download_media(youtube_url, media_type="video"):
  # Size limit: 9.216 Kb
  yt = YouTube(youtube_url, on_progress_callback=on_progress)
  stream: Stream = None

  if media_type == "video":
    # Video resolution i.e. "1080p", "720p", "480p", "360p", "240p", "144p"
    stream = yt.streams.get_highest_resolution()
    stream = yt.streams.filter(res=stream.resolution, progressive=True).first()
  elif media_type == "audio":
    stream = yt.streams.filter(only_audio=True).first()

  return stream.download()

def converter_segundos(tempo_em_segundos): 
  minutos, segundos = divmod(tempo_em_segundos, 60) 
  return f"{minutos}:{segundos:02}"

url = "https://www.youtube.com/watch?v=X3kHQzD0vKk" #(3:53) - O Rei Nasceu - Playback Legendado
url = "https://www.youtube.com/watch?v=Cc-SuLtycAo" #(8:46) - Só Tu És Santo / Uma Coisa / Deixa Queimar/ Quando Ele Vem (Ao Vivo)
url = "https://www.youtube.com/watch?v=ssdhJcW8gbQ" #(11:36) - Crie comandos de IA personalizados
url = "https://www.youtube.com/watch?v=BYFyGqCurhY" #(6:48) - Bendito Serei (Ao Vivo) (9018KB)

print('download_media: ', download_media(url, "video") )



'''
yt = YouTube(url, on_progress_callback=on_progress)
print('title: ', yt.title)
print('author: ', yt.author)
print('Length: ', yt.length)
print('Duration: ', converter_segundos(yt.length))
print('get_highest_resolution: ', yt.streams.get_highest_resolution())
print('get_audio_only: ', yt.streams.get_audio_only())#[abr]: average bitrate (audio streams only)
#print('description: ', yt.description)
for stream in yt.streams:
  print('kb: ', stream.filesize_kb ,' .::. stream: ', stream)
'''
