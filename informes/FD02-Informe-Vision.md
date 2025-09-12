# Documento de Visión - Análisis de Uso de Redes Sociales en Grupos de Telegram

<p align="center">
  <img src="../media/logo-upt.png" alt="Logo UPT" width="150">
  
  **UNIVERSIDAD PRIVADA DE TACNA**  
  **FACULTAD DE INGENIERÍA**  
  **Escuela Profesional de Ingeniería de Sistemas**
</p>

<p align="center">
  <strong>Proyecto: Análisis de Uso de Redes Sociales en Grupos de Telegram</strong>
</p>

---

**Curso:** Inteligencia de Negocios  
**Docente:** Patrick Jose Cuadros Quiroga  

**Integrantes:**
- **César Nikolas Camac Meléndez (2022074262)**
- **Jefferson Rosas Chambilla (2021072618)**

**Tacna – Perú**  
**2025**

---

## 📋 Control de Versiones

| Versión | Hecha por | Revisada por | Aprobada por | Fecha      | Motivo            |
|---------|-----------|--------------|--------------|------------|-------------------|
| 1.0     | MPV       | ELV          | ARV          | 10/10/2020 | Versión Original |

---

## 📑 Índice General

1. [Introducción](#1-introducción)
   - 1.1. [Propósito](#11-propósito)
   - 1.2. [Alcance](#12-alcance)
   - 1.3. [Definiciones, Siglas y Abreviaturas](#13-definiciones-siglas-y-abreviaturas)
   - 1.4. [Referencias](#14-referencias)
   - 1.5. [Visión General](#15-visión-general)

2. [Posicionamiento](#2-posicionamiento)
   - 2.1. [Oportunidad de Negocio](#21-oportunidad-de-negocio)
   - 2.2. [Definición del Problema](#22-definición-del-problema)

3. [Descripción de los Interesados y Usuarios](#3-descripción-de-los-interesados-y-usuarios)
   - 3.1. [Resumen de los Interesados](#31-resumen-de-los-interesados)
   - 3.2. [Resumen de los Usuarios](#32-resumen-de-los-usuarios)
   - 3.3. [Entorno de Usuario](#33-entorno-de-usuario)
   - 3.4. [Perfiles de los Interesados](#34-perfiles-de-los-interesados)
   - 3.5. [Perfiles de los Usuarios](#35-perfiles-de-los-usuarios)
   - 3.6. [Necesidades de los Interesados y Usuarios](#36-necesidades-de-los-interesados-y-usuarios)

4. [Vista General del Producto](#4-vista-general-del-producto)
   - 4.1. [Perspectiva del Producto](#41-perspectiva-del-producto)
   - 4.2. [Resumen de Capacidades](#42-resumen-de-capacidades)
   - 4.3. [Suposiciones y Dependencias](#43-suposiciones-y-dependencias)
   - 4.4. [Costos y Precios](#44-costos-y-precios)
   - 4.5. [Licenciamiento e Instalación](#45-licenciamiento-e-instalación)

5. [Características del Producto](#5-características-del-producto)

6. [Restricciones](#6-restricciones)

7. [Rangos de Calidad](#7-rangos-de-calidad)

8. [Precedencia y Prioridad](#8-precedencia-y-prioridad)

9. [Otros Requerimientos del Producto](#9-otros-requerimientos-del-producto)

10. [Conclusiones](#10-conclusiones)

11. [Recomendaciones](#11-recomendaciones)

12. [Bibliografía](#12-bibliografía)

13. [Webgrafía](#13-webgrafía)

---

## 1. Introducción

### 1.1. Propósito
Este documento define la visión del proyecto "Análisis de Uso de Redes Sociales en Grupos de Telegram", detallando los objetivos, alcance, interesados, usuarios y características principales del sistema a desarrollar para el curso de Inteligencia de Negocios.

### 1.2. Alcance
El proyecto busca analizar los enlaces compartidos en grupos de Telegram, clasificarlos según la red social de destino, obtener métricas relevantes y visualizar los resultados mediante dashboards interactivos en Power BI. El sistema abarcará la extracción, procesamiento, almacenamiento y visualización de datos.

### 1.3. Definiciones, Siglas y Abreviaturas
- **Telegram**: Plataforma de mensajería instantánea.
- **Dashboard**: Panel interactivo de visualización de datos.
- **API**: Interfaz de programación de aplicaciones.
- **Power BI**: Herramienta de visualización de datos de Microsoft.
- **PostgreSQL**: Sistema de gestión de bases de datos relacional.

### 1.4. Referencias
- Documentación oficial de Telethon.
- Documentación de Power BI.
- Documentación de APIs de redes sociales.

### 1.5. Visión General
El sistema permitirá identificar patrones de uso de redes sociales en grupos de Telegram, facilitando la toma de decisiones y el análisis exploratorio de datos para la comunidad universitaria.

---

## 2. Posicionamiento

### 2.1. Oportunidad de Negocio
El análisis de la interacción en grupos de Telegram es relevante para comprender tendencias de comunicación y difusión de contenido en redes sociales, permitiendo a instituciones y empresas optimizar sus estrategias digitales.

### 2.2. Definición del Problema
Actualmente, no existe una herramienta automatizada que permita identificar qué redes sociales son más compartidas, quiénes son los usuarios más activos y qué tipo de contenido genera mayor interacción en grupos de Telegram.

---

## 3. Descripción de los Interesados y Usuarios

### 3.1. Resumen de los Interesados
- Docente y estudiantes del curso de Inteligencia de Negocios.
- Comunidad universitaria interesada en el análisis de redes sociales.

### 3.2. Resumen de los Usuarios
- Analistas de datos.
- Estudiantes de ingeniería de sistemas.
- Docentes.

### 3.3. Entorno de Usuario
El sistema será utilizado en entornos académicos y de investigación, principalmente desde equipos con acceso a Python, Power BI y PostgreSQL.

### 3.4. Perfiles de los Interesados
- **Docente**: Supervisor y evaluador del proyecto.
- **Estudiantes**: Desarrolladores y usuarios principales.

### 3.5. Perfiles de los Usuarios
- **Usuario analista**: Interpreta los resultados y visualizaciones.
- **Usuario desarrollador**: Mantiene y mejora el sistema.

### 3.6. Necesidades de los Interesados y Usuarios
- Acceso a información clara sobre el uso de redes sociales en Telegram.
- Visualización interactiva de datos.
- Extracción automatizada y confiable de métricas.

---

## 4. Vista General del Producto

### 4.1. Perspectiva del Producto
El sistema se integra con Telegram mediante la API de Telethon, almacena datos en PostgreSQL y presenta resultados en Power BI.

### 4.2. Resumen de Capacidades
- Extracción de enlaces desde Telegram.
- Clasificación de enlaces por red social.
- Obtención de métricas de interacción.
- Identificación de usuarios más activos.
- Visualización de datos en dashboards.

### 4.3. Suposiciones y Dependencias
- Acceso a la API de Telegram y redes sociales.
- Disponibilidad de Power BI y PostgreSQL.
- Conectividad a internet.

### 4.4. Costos y Precios
El sistema utiliza herramientas mayormente gratuitas o de acceso académico.

### 4.5. Licenciamiento e Instalación
El software se desarrollará bajo licencia académica, con instalación local en los equipos de los estudiantes.

---

## 5. Características del Producto
- Extracción automática de mensajes con enlaces desde Telegram.
- Clasificación de enlaces por red social (Facebook, Instagram, TikTok, Twitter/X, YouTube, etc.).
- Obtención de métricas de interacción (likes, comentarios, fecha de publicación).
- Identificación y ranking de usuarios más activos.
- Visualización de resultados mediante dashboards en Power BI.

---

## 6. Restricciones
- Acceso limitado a APIs de redes sociales.
- Dependencia de la estructura de los mensajes de Telegram.
- Requerimiento de credenciales para acceso a grupos y APIs.

---

## 7. Rangos de Calidad
- Precisión en la extracción y clasificación de enlaces.
- Fiabilidad en la obtención de métricas.
- Interactividad y claridad en la visualización de datos.

---

## 8. Precedencia y Prioridad
1. Extracción y clasificación de enlaces.
2. Obtención de métricas.
3. Visualización de resultados.

---

## 9. Otros Requerimientos del Producto
- Cumplimiento de estándares legales y de privacidad de datos.
- Uso de buenas prácticas de desarrollo y documentación.

---

## 10. Conclusiones
El sistema propuesto permitirá analizar de manera eficiente el uso de redes sociales en grupos de Telegram, aportando valor académico y facilitando la toma de decisiones basada en datos.

---

## 11. Recomendaciones
- Ampliar el análisis a múltiples grupos y tipos de contenido.
- Implementar actualizaciones automáticas de datos.
- Considerar el análisis de sentimiento en futuras versiones.

---

## 12. Bibliografía
- Documentación oficial de Telethon, Power BI, PostgreSQL.
- Artículos académicos sobre análisis de redes sociales.

---

## 13. Webgrafía
- https://docs.telethon.dev/
- https://powerbi.microsoft.com/
- https://www.postgresql.org/
