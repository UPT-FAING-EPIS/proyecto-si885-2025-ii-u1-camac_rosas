"""
Programa base para identificar y listar todos los enlaces compartidos en un grupo de Telegram.
docker build -t telegram-links-app .
docker run -it telegram-links-app
"""

from telethon.sync import TelegramClient
import re
import requests
from bs4 import BeautifulSoup

# --- Configuración ---
api_id = '21456067'         # Reemplaza con tu API ID
api_hash = 'db863ae2aa28dc9c920a3f618c4b3dc9'     # Reemplaza con tu API Hash
session_name = 'session'     # Nombre de la sesión local

group_username = -1002686196185  # Username público o ID del grupo

# --- Conexión ---
client = TelegramClient(session_name, api_id, api_hash)
client.start()

# --- Extracción de enlaces ---
print(f"Extrayendo enlaces del grupo: {group_username}")

enlaces = []
for message in client.iter_messages(group_username):
    if message.message:
        urls = re.findall(r'(https?://[^\s]+)', message.message)
        if urls:
            enlaces.extend(urls)

redes = {
    'LinkedIn': ['linkedin.com'],
    'Dev.to': ['dev.to'],
    'YouTube': ['youtube.com', 'youtu.be'],
    'Medium': ['medium.com'],
    'Instagram': ['instagram.com'],
    'TikTok': ['tiktok.com'],
}

conteo_redes = {}
for url in enlaces:
    encontrada = False
    for nombre, dominios in redes.items():
        if any(dominio in url for dominio in dominios):
            conteo_redes[nombre] = conteo_redes.get(nombre, 0) + 1
            encontrada = True
            break
    if not encontrada:
        conteo_redes['Otra'] = conteo_redes.get('Otra', 0) + 1

# --- Listado de enlaces ---
print(f"Total de enlaces encontrados: {len(enlaces)}")
print("\nRedes sociales extraídas y concurrencia:")
for nombre, cantidad in sorted(conteo_redes.items(), key=lambda x: x[1], reverse=True):
    print(f"{nombre}: {cantidad}")

def scrap_linkedin(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Ejemplo básico, los selectores pueden cambiar
    autor = soup.find('span', {'class': 'feed-shared-actor__name'})
    autor_contenido = autor.get_text(strip=True) if autor else None
    fecha = soup.find('span', {'class': 'visually-hidden'})
    fecha_publicacion = fecha.get_text(strip=True) if fecha else None
    likes = soup.find('span', {'class': 'social-details-social-counts__reactions-count'})
    likes = likes.get_text(strip=True) if likes else None
    comentarios = soup.find('span', {'class': 'social-details-social-counts__comments'})
    comentarios = comentarios.get_text(strip=True) if comentarios else None
    return {
        'autor_contenido': autor_contenido,
        'fecha_publicacion': fecha_publicacion,
        'likes': likes,
        'comentarios': comentarios,
        # Puedes agregar más campos
    }

def scrap_youtube(url):
    # Aquí iría el scraping específico para YouTube
    return {}

def scrap_tiktok(url):
    # Aquí iría el scraping específico para TikTok
    return {}

def scrap_instagram(url):
    # Aquí iría el scraping específico para Instagram
    return {}

def scrap_medium(url):
    # Aquí iría el scraping específico para Medium
    return {}

def scrap_devto(url):
    # Aquí iría el scraping específico para Dev.to
    return {}

scrapers = {
    'LinkedIn': scrap_linkedin,
    'Dev.to': scrap_devto,
    'YouTube': scrap_youtube,
    'Medium': scrap_medium,
    'Instagram': scrap_instagram,
    'TikTok': scrap_tiktok,
}

# Procesar cada enlace y aplicar el scraper correspondiente
for url in enlaces:
    for nombre, dominios in redes.items():
        if any(dominio in url for dominio in dominios):
            datos = scrapers[nombre](url)
            print(f"\nDatos extraídos de {nombre} para el enlace:")
            print(datos)
            break

client.disconnect()
