# Use uma imagem base com Python
FROM python:3.12-slim

# Defina o diretório de trabalho
WORKDIR /app

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && apt-get clean

# Copie o arquivo de requisitos
COPY requirements.txt /app/

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o conteúdo do projeto para o diretório de trabalho
COPY . /app/

# Exponha a porta do servidor
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
