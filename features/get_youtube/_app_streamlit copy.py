import streamlit as st
from pytube import YouTube
import time

# Função para baixar vídeo ou áudio
def download_media(youtube_url, media_type="video", resolution="360p"):
    try:
        yt = YouTube(youtube_url, on_progress_callback=progress_function)

        if media_type == "video":
            # Seleciona o stream de vídeo com a resolução desejada
            stream = yt.streams.filter(res=resolution, progressive=True, file_extension="mp4").first()
            if not stream:
                stream = yt.streams.get_highest_resolution()
                st.warning(f"Resolução {resolution} não encontrada. Baixando na melhor qualidade disponível: {stream.resolution}")
        elif media_type == "audio":
            # Seleciona o stream de áudio
            stream = yt.streams.filter(only_audio=True).first()

        # Faz o download
        st.write(f"Baixando: {yt.title}")
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
media_type = st.radio("Tipo de mídia", ["Vídeo", "Áudio"])
resolution = st.selectbox("Resolução (somente para vídeo)", ["1080p", "720p", "480p", "360p"], index=1)

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
        media_choice = "video" if media_type == "Vídeo" else "audio"
        download_media(youtube_url, media_choice, resolution)
        progress_bar.progress(100)
