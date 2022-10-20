FROM python:3.8

# Cria usuario, pasta e define como proprietario
RUN useradd -ms /bin/bash user-app \
    && mkdir /app \
    && chown user-app: /app

# Instala gunicorn para ser servidor
RUN pip install gunicorn

# Instala pacotes adicionais
RUN apt update && apt install -y tesseract-ocr libtesseract-dev

# Copia os arquivos do projeto para o diretorio do app
COPY --chown=user-app web/app/ /app/

# Definindo diretorio
WORKDIR /app

# Copia arquivo de requirements
COPY web/requirements.txt requirements.txt

# Instalando os requerimentos com o PIP
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Seta variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1