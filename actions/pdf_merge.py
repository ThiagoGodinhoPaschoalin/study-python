from PyPDF2 import PdfMerger
import os

# pip install PyPDF2

def merge_pdfs(pdf_folder, output_path):
    merger = PdfMerger()
    
    # Verifica se o diretório existe
    if not os.path.exists(pdf_folder):
        raise FileNotFoundError(f"Diretório '{pdf_folder}' não encontrado")
    
    # Lista e ordena os PDFs
    pdf_files = sorted([f for f in os.listdir(pdf_folder) if f.endswith('.pdf')])
    
    # Adiciona cada PDF ao merger
    for pdf_file in pdf_files:
        full_path = os.path.join(pdf_folder, pdf_file)
        merger.append(full_path)
    
    # Salva o PDF unificado
    merger.write(output_path)
    merger.close()

# Uso prático
merge_pdfs(
    pdf_folder='PASTA_ORIGEM_DOS_PDFS',         # Pasta com PDFs individuais
    output_path='PASTA_DESTINO/TudoEmUmUnicoPdf.pdf'  # Nome do arquivo final
)
