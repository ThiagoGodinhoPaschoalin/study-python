import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Importando o módulo ttk para usar a combobox
import webbrowser
from pytubefix import YouTube, Stream
from pytubefix.cli import on_progress

def download_media(youtube_url, media_type="video"):
    yt = YouTube(youtube_url, on_progress_callback=on_progress)
    stream: Stream = None

    if media_type == "video":
        stream = yt.streams.get_highest_resolution()
        stream = yt.streams.filter(res=stream.resolution, progressive=True).first()
    elif media_type == "audio":
        stream = yt.streams.filter(only_audio=True).first()

    stream.download()


# Função para abrir a URL no navegador
def abrir_url():
    url = entrada_url.get()
    opcao = combobox_opcao.get()
    if url and opcao:
        download_media(url, opcao.lower())
        webbrowser.open(url)
        messagebox.showinfo("Informação", f"A opção selecionada foi: {opcao}")
    else:
        messagebox.showwarning("Atenção", "Por favor, insira uma URL e escolha uma opção.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Abrir URL")

# Campo de entrada para a URL
rotulo_url = tk.Label(janela, text="URL:")
rotulo_url.pack(padx=10, pady=5)
entrada_url = tk.Entry(janela, width=50)
entrada_url.pack(padx=10, pady=5)

# Campo de seleção para escolher entre Áudio ou Vídeo
rotulo_opcao = tk.Label(janela, text="Escolha uma opção:")
rotulo_opcao.pack(padx=10, pady=5)
combobox_opcao = ttk.Combobox(janela, values=["audio", "video"])
combobox_opcao.pack(padx=10, pady=5)

# Botão para abrir a URL
botao_abrir = tk.Button(janela, text="Fazer Download", command=abrir_url)
botao_abrir.pack(padx=10, pady=10)

# Iniciar o loop principal da interface gráfica
janela.mainloop()