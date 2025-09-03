# Dockerfile para la aplicación de extracción de enlaces de Telegram
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir telethon pandas beautifulsoup4 requests

# Comando por defecto para ejecutar el script principal
CMD ["python", "main.py"]
