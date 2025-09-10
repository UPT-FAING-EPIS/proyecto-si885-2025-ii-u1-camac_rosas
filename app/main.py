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

def _parse_count(value: str | None) -> int | None:
    if not value:
        return None
    txt = value.strip().replace('\xa0', ' ')
    m = re.search(r'([\d\.,]+)\s*([KkMm])?', txt)
    if not m:
        # a veces viene directamente en atributo (p.ej. "2")
        digits = re.sub(r'[^\d]', '', txt)
        return int(digits) if digits else None
    num = m.group(1).replace('.', '').replace(',', '')
    try:
        n = float(num)
    except ValueError:
        return None
    suf = m.group(2)
    if suf:
        if suf.upper() == 'K':
            n *= 1_000
        elif suf.upper() == 'M':
            n *= 1_000_000
    return int(n)

def scrap_linkedin(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    }
    try:
        resp = requests.get(url, headers=headers, timeout=20)
        resp.raise_for_status()
    except Exception:
        return {
            'autor_contenido': None,
            'likes': None,
            'comentarios': None,
            'compartidos': None,
            'visitas': None,
            'fecha_publicacion': None,
            'tipo_contenido': None,
        }

    soup = BeautifulSoup(resp.text, 'html.parser')

    # Autor: <a ... data-tracking-control-name="public_post_feed-actor-name">Nombre</a>
    autor_tag = soup.select_one('a[data-tracking-control-name="public_post_feed-actor-name"]')
    if not autor_tag:
        # Fallback genérico: cualquier <a> cuyo atributo termine en actor-name
        autor_tag = next((a for a in soup.find_all('a')
                          if a.get('data-tracking-control-name', '').endswith('actor-name')), None)
    autor_contenido = autor_tag.get_text(strip=True) if autor_tag else None

    # Likes: <span data-test-id="social-actions__reaction-count">N</span>
    likes_tag = soup.select_one('span[data-test-id="social-actions__reaction-count"]')
    likes = _parse_count(likes_tag.get_text(strip=True)) if likes_tag else 0

    # Comentarios: desde atributo data-num-comments (fallback a texto visible)
    cm_a = soup.select_one('a[data-test-id="social-actions__comments"]')
    comentarios = 0
    if cm_a:
        raw_attr = cm_a.get('data-num-comments') or cm_a.get('data-enum-comments')
        comentarios = _parse_count(raw_attr) if raw_attr else _parse_count(cm_a.get_text())

    # Fecha exacta desde JSON-LD (datePublished)
    fecha_publicacion = None
    for script in soup.find_all('script', attrs={'type': 'application/ld+json'}):
        txt = script.string or script.get_text(strip=True)
        if not txt:
            continue
        found = False
        try:
            data = json.loads(txt)
        except Exception:
            m = re.search(r'"datePublished"\s*:\s*"([^"]+)"', txt)
            if m:
                fecha_publicacion = m.group(1)
                break
            continue

        def find_date(obj) -> bool:
            nonlocal fecha_publicacion
            if isinstance(obj, dict):
                if obj.get('@type') in ('DiscussionForumPosting', 'SocialMediaPosting'):
                    if 'datePublished' in obj:
                        fecha_publicacion = obj['datePublished']
                        return True
                for v in obj.values():
                    if find_date(v):
                        return True
            elif isinstance(obj, list):
                for it in obj:
                    if find_date(it):
                        return True
            return False

        if find_date(data):
            break

    return {
        'autor_contenido': autor_contenido,
        'likes': likes,
        'comentarios': comentarios,
        'compartidos': None,
        'visitas': None,
        'fecha_publicacion': fecha_publicacion,
        'tipo_contenido': None,
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
