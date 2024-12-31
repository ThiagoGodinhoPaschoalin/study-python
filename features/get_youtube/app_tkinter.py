import tkinter as tk
from tkinter import messagebox, ttk
from tkhtmlview import HTMLLabel
from __service import download_media, get_video_info

def mostrar_info():
  url = entrada_url.get()
  if url:
    info = get_video_info(url)
    msg = f"""
Título: {info['title']}
Autor: {info['author']}
\nDuração: {info['duration']}
\nVídeo: (Limite: 9_216.0 KB)
  - Tamanho: {info['video']['filesize_kb']} KB
  - Resolução: {info['video']['resolution']}
\nÁudio: (Limite: 24_448.6 KB)
  - Tamanho: {info['audio']['filesize_kb']} KB
  - Bitrate: {info['audio']['average_bitrate']}
    """
    messagebox.showinfo("Informação", msg)
  else:
    messagebox.showwarning("Atenção", "Por favor, insira uma URL.")

def mostrar_mensagem():
  url = entrada_url.get()
  if url:
    info = get_video_info(url)
    can_video = 'green' if info['video']['can_download'] == True else 'red'
    can_audio = 'green' if info['audio']['can_download'] == True else 'red'
    # Criar uma nova janela para exibir a mensagem
    janela_mensagem = tk.Toplevel(janela)
    janela_mensagem.title("Detalhes do Vídeo")

    # HTML que será exibido
    html_content = f"""
        <br>Título: {info['title']}
        <br>Autor: {info['author']}
        <br> <p>Duração: {info['duration']}</p>
        <br><div><br>Vídeo:
          <br>- Tamanho: <span style="color: {can_video};">{info['video']['filesize_kb']}</span> KB
          <br>- Resolução: {info['video']['resolution']}</div>
        <br><div><br>Áudio:
          <br>- Tamanho: <span style="color: {can_audio};">{info['audio']['filesize_kb']}</span> KB
          <br>- Bitrate: {info['audio']['average_bitrate']}</div>
      """

    # Widget HTMLLabel para exibir o HTML
    html_label = HTMLLabel(janela_mensagem, html=html_content)
    html_label.pack(padx=10, pady=10)

    # Função para fechar a janela de mensagem
    def fechar_mensagem():
      janela_mensagem.destroy()

    # Botão para fechar a janela de mensagem
    botao_fechar = tk.Button(janela_mensagem, text="Fechar", command=fechar_mensagem)
    botao_fechar.pack(padx=10, pady=10)
  else:
    messagebox.showwarning("Atenção", "Por favor, insira uma URL.")

def iniciar_download():
  url = entrada_url.get()
  opcao = combobox_opcao.get()
  if url and opcao:
    download_media(url, opcao)
    messagebox.showinfo("Informação", "Download iniciado. Verifique a pasta de downloads.")
  else:
    messagebox.showwarning("Atenção", "Por favor, insira uma URL e escolha uma opção.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Download de Vídeos ou Áudios do YouTube - Use com responsabilidade!")
#janela.geometry("400x200")

# Campo de entrada para a URL
rotulo_url = tk.Label(janela, text="Youtube Url:", justify="right")
rotulo_url.grid(row=0, column=0, padx=10, pady=5)
entrada_url = tk.Entry(janela, width=50, justify="left")
entrada_url.grid(row=0, column=1, padx=10, pady=5)

# Campo de seleção para escolher entre Áudio ou Vídeo
rotulo_opcao = tk.Label(janela, text="Escolha uma opção:", justify="right")
rotulo_opcao.grid(row=1, column=0, padx=10, pady=5)
combobox_opcao = ttk.Combobox(janela, values=["audio", "video"], justify="left")
combobox_opcao.grid(row=1, column=1, padx=10, pady=5)

# Botão para abrir a URL e iniciar o download
botao_validar = tk.Button(janela, text="Validar", command=mostrar_mensagem)
botao_validar.grid(row=3, column=0, padx=10, pady=10)

# Botão para abrir a URL e iniciar o download
botao_download = tk.Button(janela, text="DOWNLOAD", command=iniciar_download)
botao_download.grid(row=3, column=1, padx=10, pady=10)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
