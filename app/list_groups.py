"""
list_groups.py

Script para listar todos los grupos y subgrupos de Telegram donde eres miembro, mostrando su nombre y ID.
"""

from telethon.sync import TelegramClient

# --- Configuración ---
api_id = '21456067'         # Reemplaza con tu API ID
api_hash = 'db863ae2aa28dc9c920a3f618c4b3dc9'     # Reemplaza con tu API Hash
session_name = 'session'     # Nombre de la sesión local

client = TelegramClient(session_name, api_id, api_hash)
client.start()

print("Grupos y subgrupos donde eres miembro:")
for dialog in client.iter_dialogs():
    if dialog.is_group:
        print(f"Nombre: {dialog.name} | ID: {dialog.id}")

client.disconnect()
