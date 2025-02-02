# Usa una imagen base de Python compatible con múltiples arquitecturas
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Instala Chromium y sus dependencias para Selenium
RUN apt update && apt install -y \
    chromium \
    chromium-driver \
    xvfb \
    libnss3 \
    libgconf-2-4 \
    fonts-liberation \
    libasound2 \
    wget \
    unzip \
    python3-tk \
    python3-dev && \
    apt clean && rm -rf /var/lib/apt/lists/*

# Configura una pantalla virtual para Chromium
ENV DISPLAY=:99

# Establece una variable de entorno para configurar el puerto Flask
ENV FLASK_PORT=1050

# Expone el puerto por defecto
EXPOSE ${FLASK_PORT}

# Comando por defecto para ejecutar tu aplicación
CMD ["sh", "-c", "python app.py --port=${FLASK_PORT}"]