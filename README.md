

# 📊 Proyecto de Inteligencia de Negocios

## Análisis de Uso de Redes Sociales en de Grupos de Telegram

---

## 🎓 Universidad Privada de Tacna

**Facultad de Ingeniería**
**Escuela Profesional de Ingeniería de Sistemas**

**Curso:** Inteligencia de Negocios

**Docente:** Mag. Patrick Cuadros Quiroga

---

## 👥 Integrantes del Equipo

* **César Nikolas Camac Meléndez**
* **Jefferson Ronaldihño Rosas Chambilla**

---

## ❗ Problemática

En la actualidad, los **grupos de Telegram** se han convertido en espacios de interacción masiva, donde los usuarios comparten información, enlaces y contenido de múltiples redes sociales.

Sin embargo, no siempre es sencillo responder a preguntas como:

* ¿Qué redes sociales se comparten con mayor frecuencia en estos grupos?
* ¿Quiénes son los usuarios más activos compartiendo enlaces?
* ¿Qué tipo de contenido genera mayor interacción fuera de Telegram?

---

## 🎯 Objetivo General

Analizar el **uso de redes sociales a partir de los enlaces compartidos en grupos de Telegram**, identificando patrones de comportamiento, usuarios más activos y el impacto de los enlaces en las distintas plataformas.

---

## ✅ Objetivos Específicos

* Identificar todos los enlaces compartidos en un grupo de Telegram en un periodo de tiempo.
* Clasificar los enlaces según la red social de destino (Facebook, Instagram, TikTok, Twitter/X, YouTube, etc.).
* Obtener datos de cada enlace (ej. métricas de interacción, fecha de publicación).
* Analizar a los usuarios que comparten más contenido y su nivel de participación.
* Visualizar las métricas de uso de redes sociales a través de dashboards interactivos.

---

## 🛠️ Tecnologías Utilizadas

* **Python** 🐍 → Extracción y análisis de datos.

  * Librerías: `telethon` (API de Telegram), `pandas`, `matplotlib`, `seaborn`, `requests`.
* **APIs de Redes Sociales** → Recolección de información adicional de los enlaces compartidos.
* **PostgreSQL** 🐘 → Almacenamiento estructurado de datos extraídos.
* **Power BI** 📊 → Dashboard interactivo para visualización de resultados.

---

## 📡 Metodología

1. **Conexión al grupo de Telegram**

   * Uso de `telethon` para obtener el historial de mensajes y filtrar solo los que contienen enlaces.

2. **Extracción de datos de enlaces**

   * Detección de la red social a partir de la URL.
   * Enriquecimiento de datos utilizando APIs públicas o scrapers (likes, comentarios, fecha de publicación).

3. **Procesamiento y limpieza**

   * Normalización de datos de diferentes redes sociales.
   * Identificación de usuarios más activos y frecuencia de publicaciones.

4. **Análisis de patrones**

   * Gráficas de distribución de enlaces por red social.
   * Análisis de tendencias temporales (por día, semana, mes).

5. **Visualización**

   * Creación de dashboard en Power BI mostrando:

     * Redes sociales más compartidas.
     * Top usuarios que publican enlaces.
     * Tendencias de actividad en el tiempo.

---

## 📊 Ejemplo de Visualizaciones

* **Gráfico de barras** con la cantidad de enlaces por red social.
* **Gráfico de líneas** mostrando la evolución de la cantidad de enlaces compartidos a lo largo del tiempo.
* **Ranking de usuarios más activos** compartiendo contenido.
* **Mapa de calor** de actividad por hora del día.

---

## 🚀 Resultados Esperados

* Identificación de qué redes sociales son más populares en los grupos de Telegram analizados.
* Perfil de los usuarios más influyentes (mayor cantidad de enlaces compartidos).
* Detección de patrones de uso y horarios de mayor actividad.
* Dashboard interactivo que permita realizar análisis exploratorio de los datos.

---

## 📎 Enlace al Dashboard

🔗 [Acceder al Dashboard en Power BI](https://app.powerbi.com/) *(se añadirá el link final una vez publicado)*

---

## 📌 Roadmap Futuro

* Ampliar el análisis a múltiples grupos de Telegram simultáneamente.
* Clasificar el tipo de contenido (videos, imágenes, artículos).
* Realizar análisis de sentimiento de los comentarios de las publicaciones compartidas.
* Implementar un sistema automatizado que recolecte y actualice datos en tiempo real.

