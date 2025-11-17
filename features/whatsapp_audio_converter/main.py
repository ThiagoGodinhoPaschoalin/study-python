import os
import sys
from pydub import AudioSegment
import logging

# Configuração básica de log para exibir mensagens de erro
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def converter_ogg_para_mp3(caminho_pasta):
    """
    Converte todos os arquivos .ogg em um diretório para .mp3.

    Args:
        caminho_pasta (str): O caminho absoluto ou relativo para a pasta contendo os arquivos .ogg.
    """
    if not os.path.isdir(caminho_pasta):
        logging.error(f"O caminho especificado não é um diretório válido: {caminho_pasta}")
        return

    arquivos_encontrados = 0
    arquivos_convertidos = 0

    logging.info(f"Iniciando a conversão na pasta: {caminho_pasta}")

    # Percorre todos os itens no diretório
    for nome_arquivo in os.listdir(caminho_pasta):
        # Verifica se o arquivo tem a extensão .ogg e se é um arquivo (e não uma pasta)
        if nome_arquivo.endswith('.ogg') and os.path.isfile(os.path.join(caminho_pasta, nome_arquivo)):
            arquivos_encontrados += 1
            
            # Constrói o caminho completo dos arquivos
            caminho_ogg = os.path.join(caminho_pasta, nome_arquivo)
            
            # Cria o nome do novo arquivo .mp3
            nome_base = os.path.splitext(nome_arquivo)[0]
            caminho_mp3 = os.path.join(caminho_pasta, f"{nome_base}.mp3")

            logging.info(f"Processando: {nome_arquivo} -> {nome_base}.mp3")
            
            try:
                # Carrega o arquivo OGG
                audio = AudioSegment.from_ogg(caminho_ogg)
                
                # Exporta como MP3. O bitrate (bitrate="192k") é opcional e define a qualidade.
                audio.export(caminho_mp3, format="mp3", bitrate="192k")
                
                logging.info(f"Sucesso! Salvo como: {nome_base}.mp3")
                arquivos_convertidos += 1
                
            except FileNotFoundError:
                # Este erro geralmente ocorre se o FFmpeg não estiver instalado/acessível
                logging.error("Erro: O FFmpeg não foi encontrado. Certifique-se de que está instalado e no PATH.")
                break # Para o loop se o FFmpeg não for encontrado
            except Exception as e:
                logging.error(f"Erro ao processar o arquivo {nome_arquivo}: {e}")

    logging.info(f"\n--- Resumo da Conversão ---")
    logging.info(f"Arquivos .ogg encontrados: {arquivos_encontrados}")
    logging.info(f"Arquivos .mp3 criados: {arquivos_convertidos}")
    if arquivos_encontrados > 0 and arquivos_convertidos == 0:
        logging.warning("Nenhuma conversão foi concluída. Verifique os erros acima.")

# --- Uso do Script ---
# Mude este caminho para o diretório onde você salvou os áudios do WhatsApp!
# Ou passe como argumento: python3 main.py /caminho/para/pasta
PASTA_AUDIOS = "/home/public/Downloads/whatsapp_audios" 

if __name__ == "__main__":
    if len(sys.argv) > 1:
        PASTA_AUDIOS = sys.argv[1]
    converter_ogg_para_mp3(PASTA_AUDIOS)