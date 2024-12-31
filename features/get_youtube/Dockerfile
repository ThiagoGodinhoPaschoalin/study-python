FROM python:3.11-slim

WORKDIR /app

RUN apt update && apt upgrade -y
RUN python -m pip install --upgrade pip

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
COPY ./app_streamlit.py /app/main.py

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]