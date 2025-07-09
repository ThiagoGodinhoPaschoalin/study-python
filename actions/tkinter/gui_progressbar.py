import tkinter as tk
from tkinter import ttk, messagebox
import time

# Função para simular o download e atualizar a barra de progresso
def iniciar_download():
    progresso['value'] = 0
    janela.update_idletasks()
    for i in range(1, 101):
        time.sleep(0.05)  # Simula o tempo de download
        progresso['value'] = i
        janela.update_idletasks()
    messagebox.showinfo("Informação", "Download concluído!")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Barra de Progresso de Download")

# Barra de progresso
progresso = ttk.Progressbar(janela, orient="horizontal", length=300, mode="determinate")
progresso.pack(padx=20, pady=20)

# Botão para iniciar o download
botao_iniciar = tk.Button(janela, text="Iniciar Download", command=iniciar_download)
botao_iniciar.pack(padx=20, pady=20)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
