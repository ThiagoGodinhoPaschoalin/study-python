from pytubefix import YouTube, Stream
from pytubefix.cli import on_progress

# https://github.com/JuanBindez/pytubefix
# https://pytubefix.readthedocs.io/en/latest
# pip install pytubefix

url = "https://www.youtube.com/watch?v=X3kHQzD0vKk"
url = "https://www.youtube.com/watch?v=-U88YhDBJ2Q"

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title, '\n', yt.author)

# audio or video
choice = 'video'
ys: Stream = None

if choice == 'video':
    stream = yt.streams.get_highest_resolution()
    print('Melhor resolução: ', stream.resolution) # "360p", "480p", "720p", "1080p"
    ys = yt.streams.filter(res=stream.resolution, progressive=True).first()
elif choice == 'audio':
    ys = yt.streams.filter(only_audio=True).first()
else:
    print('não escolhido')

print(choice, "\n", ys.download())