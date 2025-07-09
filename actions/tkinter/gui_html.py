import tkinter as tk
from tkhtmlview import HTMLLabel

def mostrar_mensagem():
    # Criar uma nova janela para exibir a mensagem
    janela_mensagem = tk.Toplevel(janela)
    janela_mensagem.title("Mensagem HTML")

    # HTML que será exibido
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Texto Colorido</title>
    </head>
    <body>
        <p>Este é um <span style="color: red;">texto vermelho</span>.</p>
        <p>Este é um <span style="color: blue;">texto azul</span>.</p>
        <p>Este é um <span style="color: green;">texto verde</span>.</p>
    </body>
    </html>
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

# Configuração da janela principal
janela = tk.Tk()
janela.title("Exibição de HTML com Tkinter")

# Botão para mostrar a mensagem HTML
botao_mensagem = tk.Button(janela, text="Mostrar Mensagem", command=mostrar_mensagem)
botao_mensagem.pack(padx=10, pady=10)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
