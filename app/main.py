"""
Programa base para identificar y listar todos los enlaces compartidos en un grupo de Telegram.
docker build -t telegram-links-app .
docker run -it telegram-links-app
"""

from telethon.sync import TelegramClient
import re

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
        urls = re.findall(r'(https?://[\w\.-/\?=&%#]+)', message.message)
        if urls:
            enlaces.extend(urls)

# --- Listado de enlaces ---
print(f"Total de enlaces encontrados: {len(enlaces)}")
for url in enlaces:
    print(url)

client.disconnect()
