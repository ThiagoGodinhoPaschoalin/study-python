import streamlit as st
from pytubefix import YouTube, Stream

# Função para baixar vídeo ou áudio
def download_media(youtube_url, media_type="video"):
    try:
        yt = YouTube(youtube_url, on_progress_callback=progress_function)
        stream: Stream = None

        if media_type == "video":
            stream = yt.streams.get_highest_resolution()
            stream = yt.streams.filter(res=stream.resolution, progressive=True).first()
        elif media_type == "audio":
            stream = yt.streams.filter(only_audio=True).first()

        # Faz o download
        st.write(f"Baixando {media_type}: {yt.title}")
        stream.download()
        st.success(f"Download concluído: {yt.title}")
    except Exception as e:
        st.error(f"Erro ao baixar: {e}")

# Função de callback para atualizar a barra de progresso
def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = bytes_downloaded / total_size
    st.session_state.progress = progress * 100  # Atualiza a barra de progresso

# Configuração da interface do Streamlit
st.title("Download de Vídeos ou Áudios do YouTube")
st.write("Cole o link do vídeo do YouTube abaixo, escolha o formato e clique em 'Fazer Download'.")

# Input do usuário
youtube_url = st.text_input("URL do vídeo no YouTube", "")
media_type = st.radio("Tipo de mídia", ["video", "audio"])

# Barra de progresso
if "progress" not in st.session_state:
    st.session_state.progress = 0
progress_bar = st.progress(st.session_state.progress)

# Botão para iniciar o download
if st.button("Fazer Download"):
    if not youtube_url.strip():
        st.warning("Por favor, insira um URL válido.")
    else:
        st.session_state.progress = 0
        download_media(youtube_url, media_type)
        progress_bar.progress(100)
