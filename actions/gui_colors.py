import tkinter as tk
from tkinter import ttk

# Função para adicionar texto colorido
def adicionar_texto_colorido():
    texto.tag_config("vermelho", foreground="red")
    texto.tag_config("azul", foreground="blue")
    
    texto.insert(tk.END, "Este texto é normal.\n")
    texto.insert(tk.END, "Este texto é vermelho.\n", "vermelho")
    texto.insert(tk.END, "Este texto é azul.\n", "azul")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Texto Colorido com Tkinter")

# Widget Text para exibir texto formatado
texto = tk.Text(janela, height=10, width=50)
texto.pack(padx=10, pady=10)

# Botão para adicionar texto colorido
botao_adicionar = tk.Button(janela, text="Adicionar Texto Colorido", command=adicionar_texto_colorido)
botao_adicionar.pack(padx=10, pady=10)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
