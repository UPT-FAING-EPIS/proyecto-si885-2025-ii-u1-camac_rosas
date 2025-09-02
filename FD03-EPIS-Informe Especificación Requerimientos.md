<center>

![./media/logo-upt.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERIA**

**Escuela Profesional de Ingeniería de Sistemas**

**Proyecto Análisis de Uso de Redes Sociales en de Grupos de Telegram**

Curso: Inteligencia de Negocios

Docente: Patrick Jose Cuadros Quiroga

Integrantes:

**César Nikolas Camac Meléndez (2022074262)**

**Jefferson Rosas Chambilla (2021072618)**

**Tacna – Perú**

**2025**

</center>
<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

|CONTROL DE VERSIONES||||||
| :-: | :- | :- | :- | :- | :- |
|Versión|Hecha por|Revisada por|Aprobada por|Fecha|Motivo|
|1\.0|MPV|ELV|ARV|10/10/2020|Versión Original|

**Sistema Análisis de Uso de Redes Sociales en de Grupos de Telegram**

**Documento de Especificación de Requerimientos de Software**

**Versión *1.0***

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

|CONTROL DE VERSIONES||||||
| :-: | :- | :- | :- | :- | :- |
|Versión|Hecha por|Revisada por|Aprobada por|Fecha|Motivo|
|1\.0|MPV|ELV|ARV|10/10/2020|Versión Original|

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

**INDICE GENERAL**
#
1.  [INTRODUCCION](#introduccion)
2.  [Generalidades de la Empresa](#generalidades-de-la-empresa)
    2.1. Nombre de la Empresa
    2.2. Visión
    2.3. Misión
    2.4. Organigrama
3.  [Visión del Negocio](#vision-del-negocio)
    3.1. Descripción del Problema
    3.2. Objetivos de Negocios
    3.3. Objetivos de Diseño
    3.4. Alcance del proyecto
    3.5. Viabilidad del Sistema
    3.6. Información obtenida del Levantamiento de Información
4.  [Análisis de Procesos](#analisis-de-procesos)
    4.1. Diagrama del Proceso Actual – Diagrama de actividades
    4.2. Diagrama del Proceso Propuesto – Diagrama de actividades Inicial
5.  [Especificación de Requerimientos de Software](#especificacion-de-requerimientos-de-software)
    5.1. Cuadro de Requerimientos funcionales Inicial
    5.2. Cuadro de Requerimientos No funcionales
    5.3. Cuadro de Requerimientos funcionales Final
    5.4. Reglas de Negocio
6.  [Fase de Desarrollo](#fase-de-desarrollo)
    6.1. Perfiles de Usuario
    6.2. Modelo Conceptual
    6.3. Diagrama de Paquetes
    6.4. Diagrama de Casos de Uso
    6.5. Escenarios de Caso de Uso (narrativa)
7.  [Modelo Lógico](#modelo-logico)
    7.1. Análisis de Objetos
    7.2. Diagrama de Actividades con objetos
    7.3. Diagrama de Secuencia
    7.4. Diagrama de Clases
8.  [CONCLUSIONES](#conclusiones)
9.  [RECOMENDACIONES](#recomendaciones)
10. [BIBLIOGRAFIA](#bibliografia)
11. [WEBGRAFIA](#webgrafia)

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## <a name="introduccion"></a>INTRODUCCIÓN

El propósito de este documento es detallar los requerimientos de software para el proyecto **"Análisis de Uso de Redes Sociales en Grupos de Telegram"**. Se definen los objetivos, el alcance, las características y las restricciones del sistema para guiar el proceso de desarrollo.

---

## <a name="generalidades-de-la-empresa"></a>GENERALIDADES DE LA EMPRESA

### 2.1. Nombre de la Empresa
El proyecto se desarrolla en el contexto de la **Universidad Privada de Tacna**, específicamente en la **Escuela Profesional de Ingeniería de Sistemas**.

### 2.2. Visión
El sistema permitirá identificar patrones de uso de redes sociales en grupos de Telegram, facilitando la toma de decisiones y el análisis exploratorio de datos para la comunidad universitaria.

### 2.3. Misión
Desarrollar una herramienta de inteligencia de negocios para analizar el comportamiento y la interacción digital dentro de grupos de Telegram, proporcionando información valiosa para la academia y la investigación.

### 2.4. Organigrama
* **Docente**: Supervisor y evaluador del proyecto.
* **Estudiantes (Desarrolladores)**: Encargados del diseño, desarrollo y mantenimiento del sistema.

---

## <a name="vision-del-negocio"></a>VISIÓN DEL NEGOCIO

### 3.1. Descripción del Problema
No existe una herramienta automatizada que permita identificar qué redes sociales son más compartidas, quiénes son los usuarios más activos y qué tipo de contenido genera mayor interacción en grupos de Telegram.

### 3.2. Objetivos de Negocios
* Comprender las tendencias de comunicación y difusión de contenido en grupos de Telegram.
* Optimizar estrategias digitales para instituciones y empresas.
* Facilitar el análisis exploratorio de datos para la comunidad académica.

### 3.3. Objetivos de Diseño
* Crear una solución escalable y confiable para la extracción de datos.
* Proporcionar visualizaciones interactivas y fáciles de entender.
* Asegurar la precisión en la clasificación y las métricas obtenidas.

### 3.4. Alcance del proyecto
El proyecto abarca la **extracción**, **procesamiento**, **almacenamiento** y **visualización** de datos de enlaces compartidos en grupos de Telegram. El análisis se centrará en la clasificación de enlaces por red social y la obtención de métricas de interacción.

### 3.5. Viabilidad del Sistema
El sistema es factible debido a que utiliza herramientas de acceso académico y mayormente gratuitas (Python, Power BI, PostgreSQL), además de aprovechar la API de Telethon para la extracción de datos.

### 3.6. Información obtenida del Levantamiento de Información
Se identificó la necesidad de una herramienta para analizar la interacción en grupos de Telegram, ya que las plataformas existentes no ofrecen un enfoque específico en este tipo de mensajería instantánea.

---

## <a name="analisis-de-procesos"></a>ANÁLISIS DE PROCESOS

### 4.1. Diagrama del Proceso Actual – Diagrama de actividades
**Proceso manual de análisis:**
1.  Un usuario accede a un grupo de Telegram.
2.  El usuario busca manualmente mensajes con enlaces.
3.  El usuario copia los enlaces y los visita uno por uno.
4.  El usuario revisa las métricas de interacción (ej. likes, comentarios) manualmente.
5.  El usuario anota los datos en una hoja de cálculo.
6.  El usuario crea gráficos manualmente para el análisis.

### 4.2. Diagrama del Proceso Propuesto – Diagrama de actividades Inicial
**Proceso automatizado del sistema:**
1.  El **Sistema** se conecta a un grupo de Telegram usando la API de Telethon.
2.  El **Sistema** extrae los mensajes que contienen enlaces.
3.  El **Sistema** clasifica los enlaces por red social.
4.  El **Sistema** obtiene las métricas de interacción de cada enlace.
5.  El **Sistema** almacena los datos en la base de datos PostgreSQL.
6.  **Power BI** se conecta a la base de datos y visualiza los resultados en dashboards interactivos.
7.  El **Usuario Analista** interpreta los resultados en los dashboards.

---

## <a name="especificacion-de-requerimientos-de-software"></a>ESPECIFICACIÓN DE REQUERIMIENTOS DE SOFTWARE

### 5.1. Cuadro de Requerimientos funcionales Inicial
| ID | Requerimiento Funcional | Prioridad |
| :-: | :--- | :-: |
| RF01 | El sistema debe extraer automáticamente mensajes con enlaces desde Telegram. | Alta |
| RF02 | El sistema debe clasificar los enlaces por red social (Facebook, Instagram, TikTok, etc.). | Alta |
| RF03 | El sistema debe obtener métricas de interacción (likes, comentarios, fecha). | Media |
| RF04 | El sistema debe identificar y clasificar a los usuarios más activos. | Media |
| RF05 | El sistema debe almacenar los datos extraídos en una base de datos relacional. | Alta |
| RF06 | El sistema debe generar un conjunto de datos compatible con Power BI. | Alta |
| RF07 | El sistema debe visualizar los resultados en dashboards interactivos. | Alta |

### 5.2. Cuadro de Requerimientos No funcionales
| ID | Requerimiento No Funcional | Prioridad |
| :-: | :--- | :-: |
| RNF01 | **Rendimiento:** El sistema debe procesar un volumen de 1000 mensajes con enlaces en menos de 5 minutos. | Media |
| RNF02 | **Usabilidad:** Los dashboards de Power BI deben ser intuitivos y fáciles de usar para los usuarios analistas. | Alta |
| RNF03 | **Fiabilidad:** La extracción y clasificación de enlaces debe tener una precisión superior al 95%. | Alta |
| RNF04 | **Seguridad:** El sistema debe manejar las credenciales de acceso a Telegram y APIs de manera segura. | Alta |
| RNF05 | **Escalabilidad:** El sistema debe ser capaz de procesar más de un grupo de Telegram simultáneamente en futuras versiones. | Baja |

### 5.3. Cuadro de Requerimientos funcionales Final
El cuadro final es idéntico al inicial en esta fase del proyecto, ya que se encuentra en una etapa de desarrollo inicial. Los requerimientos no han sido modificados.

### 5.4. Reglas de Negocio
* Solo se considerarán los mensajes que contengan al menos un enlace web (`http://` o `https://`).
* Los enlaces que no correspondan a las redes sociales definidas (Facebook, Instagram, TikTok, Twitter/X, YouTube) se clasificarán como "Otros".
* La identificación de usuarios activos se basará en la cantidad de enlaces únicos que cada usuario ha compartido.
* Las métricas de interacción se obtendrán directamente de las APIs de las redes sociales correspondientes, si el acceso lo permite.

---

## <a name="fase-de-desarrollo"></a>FASE DE DESARROLLO

### 6.1. Perfiles de Usuario
* **Usuario Analista**: Se interesa en la interpretación de los datos y el análisis de las tendencias. Necesita visualizaciones claras e interactivas.
* **Usuario Desarrollador**: Encargado de mantener y mejorar el sistema. Se enfoca en la extracción, el procesamiento de datos y la integración entre componentes.

### 6.2. Modelo Conceptual
El sistema se compone de tres módulos principales que interactúan entre sí:
* **Módulo de Extracción**: Extrae los datos de Telegram.
* **Módulo de Almacenamiento**: Gestiona la base de datos.
* **Módulo de Visualización**: Presenta los datos al usuario.

### 6.3. Diagrama de Paquetes
* `com.upt.project.extraction`: Contiene las clases y funciones para la extracción de datos de Telegram.
* `com.upt.project.processing`: Contiene las funciones de clasificación de enlaces y obtención de métricas.
* `com.upt.project.database`: Contiene las clases de conexión y manipulación de la base de datos PostgreSQL.
* `com.upt.project.visualization`: Contiene los archivos de Power BI para la representación de datos.

### 6.4. Diagrama de Casos de Uso
**Caso de Uso: Analizar datos de Telegram**
* **Actor**: Usuario Analista
* **Descripción**: El usuario accede al dashboard en Power BI para visualizar los datos procesados por el sistema.
* **Precondiciones**: El sistema ha extraído, procesado y almacenado los datos en la base de datos.
* **Flujo Normal**:
    1. El usuario abre el dashboard de Power BI.
    2. El dashboard se actualiza automáticamente con los datos de PostgreSQL.
    3. El usuario interactúa con los gráficos para filtrar y analizar la información.

**Caso de Uso: Extraer enlaces de un grupo**
* **Actor**: Usuario Desarrollador
* **Descripción**: El desarrollador ejecuta el script de extracción para obtener los mensajes de un grupo de Telegram.
* **Precondiciones**: El desarrollador tiene acceso a las credenciales de Telegram y el script está configurado correctamente.
* **Flujo Normal**:
    1. El desarrollador ejecuta el script de extracción.
    2. El script se conecta a Telegram y extrae los mensajes.
    3. El script guarda los datos en la base de datos para su posterior procesamiento.

### 6.5. Escenarios de Caso de Uso (narrativa)
**Escenario de Extracción y Almacenamiento:**
* **Nombre**: Proceso de ETL diario.
* **Actores**: Usuario Desarrollador, Sistema.
* **Pasos**:
    1.  El **Desarrollador** inicia el script de extracción a las 00:00 (o de forma manual).
    2.  El **Sistema** se conecta a la API de Telegram y lee los mensajes nuevos del grupo "Marketing Digital UPT".
    3.  El **Sistema** identifica todos los mensajes con enlaces y los clasifica.
    4.  El **Sistema** obtiene el número de likes y comentarios de cada enlace.
    5.  El **Sistema** inserta los datos limpios y enriquecidos en la base de datos **PostgreSQL**.
    6.  El **Desarrollador** verifica que el proceso se haya completado sin errores.

**Escenario de Visualización de Datos:**
* **Nombre**: Consulta de tendencias semanales.
* **Actores**: Usuario Analista, Power BI.
* **Pasos**:
    1.  El **Analista** abre el informe de **Power BI** en su equipo.
    2.  **Power BI** refresca los datos desde la base de datos **PostgreSQL**.
    3.  El **Analista** selecciona un filtro de fecha de "Últimos 7 días".
    4.  El gráfico de "Redes Sociales Más Compartidas" se actualiza para mostrar que YouTube fue la más popular.
    5.  El **Analista** filtra por "YouTube" para ver los usuarios que más compartieron enlaces de esa plataforma.
    6.  El **Analista** descubre que el usuario "Juan" fue el más activo.

---

## <a name="modelo-logico"></a>MODELO LÓGICO

### 7.1. Análisis de Objetos
* **Mensaje**: Objeto que representa un mensaje de Telegram. Atributos: `id_mensaje`, `autor_id`, `fecha`, `contenido`.
* **Enlace**: Objeto que representa un enlace extraído. Atributos: `url`, `red_social`, `titulo_contenido`, `likes`, `comentarios`, `fecha_publicacion`.
* **Usuario**: Objeto que representa un usuario de Telegram. Atributos: `id_usuario`, `nombre`, `cantidad_enlaces_compartidos`.

### 7.2. Diagrama de Actividades con objetos
(Este apartado requiere un diagrama visual. Se describe el flujo de objetos).
1.  **[Mensaje]** -> **Extraer Enlace** -> **[Enlace]**
2.  **[Enlace]** -> **Clasificar Red Social** -> **[Enlace clasificado]**
3.  **[Enlace clasificado]** -> **Obtener Métricas** -> **[Enlace con métricas]**
4.  **[Enlace con métricas]** -> **Guardar en BD** -> **[Datos en PostgreSQL]**
5.  **[Datos en PostgreSQL]** -> **Visualizar en Dashboard** -> **[Dashboard de Power BI]**

### 7.3. Diagrama de Secuencia
(Este apartado requiere un diagrama visual. Se describe la secuencia de llamadas).
1.  `Script de Extracción` -> `Telegram API`: **getMessages()**
2.  `Telegram API` -> `Script de Extracción`: **[Mensajes]**
3.  `Script de Extracción` -> `Procesador`: **processLinks([Mensajes])**
4.  `Procesador` -> `Red Social API`: **getMetrics(enlace)**
5.  `Red Social API` -> `Procesador`: **[Métricas]**
6.  `Procesador` -> `BD_PostgreSQL`: **saveData([Datos])**
7.  `Usuario` -> `Power BI`: **viewDashboard()**
8.  `Power BI` -> `BD_PostgreSQL`: **queryData()**
9.  `BD_PostgreSQL` -> `Power BI`: **[Resultados]**

### 7.4. Diagrama de Clases
(Este apartado requiere un diagrama visual. Se describen las clases y sus relaciones).
* **Clase `Mensaje`**: id_mensaje, autor_id, fecha, contenido.
* **Clase `Enlace`**: url, red_social, likes, comentarios, fecha_publicacion.
* **Clase `Usuario`**: id_usuario, nombre.
* **Relación**: `Usuario` "Comparte" `Mensaje`. `Mensaje` "Contiene" `Enlace`.

---

## <a name="conclusiones"></a>CONCLUSIONES

El sistema propuesto permitirá analizar de manera eficiente el uso de redes sociales en grupos de Telegram, aportando valor académico y facilitando la toma de decisiones basada en datos. Los requerimientos definidos establecen una base sólida para el desarrollo.

---

## <a name="recomendaciones"></a>RECOMENDACIONES

Se recomienda **ampliar el análisis a múltiples grupos y tipos de contenido** e **implementar actualizaciones automáticas de datos**. También se sugiere **considerar el análisis de sentimiento** en futuras versiones para obtener una comprensión más profunda de la interacción.

---

## <a name="bibliografia"></a>BIBLIOGRAFÍA

* Documentación oficial de Telethon, Power BI, PostgreSQL.
* Artículos académicos sobre análisis de redes sociales.

---

## <a name="webgrafia"></a>WEBGRAFÍA

* https://docs.telethon.dev/
* https://powerbi.microsoft.com/
* https://www.postgresql.org/
