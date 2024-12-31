# Docker 

A versão 3.11.11 do python foi a última testada e aprovada pela biblioteca neste momento

> Acessar o contêiner. Para quando não quer ter python instalado na sua máquina
```bash
docker pull python:3.11-slim
docker rm study-python
docker run --name study-python -it python:3.11-slim bash
```

> Gerar imagem da funcionalidade
```bash
cd ./features/get_youtube
docker build -t study-python:3.11-get_youtube -f ./Dockerfile .
docker run -p 8501:8501 --name get_youtube study-python:3.11-get_youtube
```

# Processo de execução

```bash
pip install streamlit pytubefix pydub ffmpeg
```

# Gerar executável:

> Como eu estou dentro de uma variavel de ambiente, para mitigar mal funcionamento, execute os comandos num terminal externo. 

```bash
cd C:\.repositories\mvp\study-python\features\get_youtube
mkdir -p executable/.venv_exe
cd ./executable
python -m venv .\.venv_exe
.\.venv_exe\Scripts\Activate
pip install pytubefix tkhtmlview pyinstaller
pyinstaller --onefile --noconsole ../app_tkinter.py
```
