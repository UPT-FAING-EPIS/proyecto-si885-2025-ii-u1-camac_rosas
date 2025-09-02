<center>

[comment]: <img src="./media/media/image1.png" style="width:1.088in;height:1.46256in" alt="escudo.png" />

![./media/media/image1.png](./media/logo-upt.png)

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












**Proyecto Análisis de Uso de Redes Sociales en de Grupos de Telegram**

**Documento de Visión**

**Versión *1.0***
**

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

|CONTROL DE VERSIONES||||||
| :-: | :- | :- | :- | :- | :- |
|Versión|Hecha por|Revisada por|Aprobada por|Fecha|Motivo|
|1\.0|MPV|ELV|ARV|10/10/2020|Versión Original|


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>


**INDICE GENERAL**
#
[1.	Introducción](#_Toc52661346)

1.1	Propósito

1.2	Alcance

1.3	Definiciones, Siglas y Abreviaturas

1.4	Referencias

1.5	Visión General

[2.	Posicionamiento](#_Toc52661347)

2.1	Oportunidad de negocio

2.2	Definición del problema

[3.	Descripción de los interesados y usuarios](#_Toc52661348)

3.1	Resumen de los interesados

3.2	Resumen de los usuarios

3.3	Entorno de usuario

3.4	Perfiles de los interesados

3.5	Perfiles de los Usuarios

3.6	Necesidades de los interesados y usuarios

[4.	Vista General del Producto](#_Toc52661349)

4.1	Perspectiva del producto

4.2	Resumen de capacidades

4.3	Suposiciones y dependencias

4.4	Costos y precios

4.5	Licenciamiento e instalación

[5.	Características del producto](#_Toc52661350)

[6.	Restricciones](#_Toc52661351)

[7.	Rangos de calidad](#_Toc52661352)

[8.	Precedencia y Prioridad](#_Toc52661353)

[9.	Otros requerimientos del producto](#_Toc52661354)

b) Estandares legales

c) Estandares de comunicación	](#_toc394513800)37

d) Estandaraes de cumplimiento de la plataforma	](#_toc394513800)42

e) Estandaraes de calidad y seguridad	](#_toc394513800)42

[CONCLUSIONES](#_Toc52661355)

[RECOMENDACIONES](#_Toc52661356)

[BIBLIOGRAFIA](#_Toc52661357)

[WEBGRAFIA](#_Toc52661358)


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

**<u>Informe de Visión</u>**

1. <span id="_Toc52661346" class="anchor"></span>**Introducción**

    **1.1 Propósito**
    El propósito de este documento es definir la visión del proyecto “Análisis de Uso de Redes Sociales en Grupos de Telegram”, detallando los objetivos, alcance, interesados, usuarios y características principales del sistema a desarrollar para el curso de Inteligencia de Negocios.

    **1.2 Alcance**
    El proyecto busca analizar los enlaces compartidos en grupos de Telegram, clasificarlos según la red social de destino, obtener métricas relevantes y visualizar los resultados mediante dashboards interactivos en Power BI. El sistema abarcará la extracción, procesamiento, almacenamiento y visualización de datos.

    **1.3 Definiciones, Siglas y Abreviaturas**
    - **Telegram**: Plataforma de mensajería instantánea.
    - **Dashboard**: Panel interactivo de visualización de datos.
    - **API**: Interfaz de programación de aplicaciones.
    - **Power BI**: Herramienta de visualización de datos de Microsoft.
    - **PostgreSQL**: Sistema de gestión de bases de datos relacional.

    **1.4 Referencias**
    - Documentación oficial de Telethon.
    - Documentación de Power BI.
    - Documentación de APIs de redes sociales.

    **1.5 Visión General**
    El sistema permitirá identificar patrones de uso de redes sociales en grupos de Telegram, facilitando la toma de decisiones y el análisis exploratorio de datos para la comunidad universitaria.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

2. <span id="_Toc52661347" class="anchor"></span>**Posicionamiento**

    **2.1 Oportunidad de negocio**
    El análisis de la interacción en grupos de Telegram es relevante para comprender tendencias de comunicación y difusión de contenido en redes sociales, permitiendo a instituciones y empresas optimizar sus estrategias digitales.

    **2.2 Definición del problema**
    Actualmente, no existe una herramienta automatizada que permita identificar qué redes sociales son más compartidas, quiénes son los usuarios más activos y qué tipo de contenido genera mayor interacción en grupos de Telegram.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

3. <span id="_Toc52661348" class="anchor"></span>**Vista General del Producto**

    **3.1 Resumen de los interesados**
    - Docente y estudiantes del curso de Inteligencia de Negocios.
    - Comunidad universitaria interesada en el análisis de redes sociales.

    **3.2 Resumen de los usuarios**
    - Analistas de datos.
    - Estudiantes de ingeniería de sistemas.
    - Docentes.

    **3.3 Entorno de usuario**
    El sistema será utilizado en entornos académicos y de investigación, principalmente desde equipos con acceso a Python, Power BI y PostgreSQL.

    **3.4 Perfiles de los interesados**
    - Docente: Supervisor y evaluador del proyecto.
    - Estudiantes: Desarrolladores y usuarios principales.

    **3.5 Perfiles de los Usuarios**
    - Usuario analista: Interpreta los resultados y visualizaciones.
    - Usuario desarrollador: Mantiene y mejora el sistema.

    **3.6 Necesidades de los interesados y usuarios**
    - Acceso a información clara sobre el uso de redes sociales en Telegram.
    - Visualización interactiva de datos.
    - Extracción automatizada y confiable de métricas.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

4. <span id="_Toc52661349" class="anchor"></span>**Estudio de
    Factibilidad**

    **4.1 Perspectiva del producto**
    El sistema se integra con Telegram mediante la API de Telethon, almacena datos en PostgreSQL y presenta resultados en Power BI.

    **4.2 Resumen de capacidades**
    - Extracción de enlaces desde Telegram.
    - Clasificación de enlaces por red social.
    - Obtención de métricas de interacción.
    - Identificación de usuarios más activos.
    - Visualización de datos en dashboards.

    **4.3 Suposiciones y dependencias**
    - Acceso a la API de Telegram y redes sociales.
    - Disponibilidad de Power BI y PostgreSQL.
    - Conectividad a internet.

    **4.4 Costos y precios**
    El sistema utiliza herramientas mayormente gratuitas o de acceso académico.

    **4.5 Licenciamiento e instalación**
    El software se desarrollará bajo licencia académica, con instalación local en los equipos de los estudiantes.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

5. <span id="_Toc52661350" class="anchor"></span>**Características del producto**

    - Extracción automática de mensajes con enlaces desde Telegram.
    - Clasificación de enlaces por red social (Facebook, Instagram, TikTok, Twitter/X, YouTube, etc.).
    - Obtención de métricas de interacción (likes, comentarios, fecha de publicación).
    - Identificación y ranking de usuarios más activos.
    - Visualización de resultados mediante dashboards en Power BI.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

6. <span id="_Toc52661351" class="anchor"></span>**Restricciones**

    - Acceso limitado a APIs de redes sociales.
    - Dependencia de la estructura de los mensajes de Telegram.
    - Requerimiento de credenciales para acceso a grupos y APIs.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

7. <span id="_Toc52661352" class="anchor"></span>**Rangos de Calidad**

    - Precisión en la extracción y clasificación de enlaces.
    - Fiabilidad en la obtención de métricas.
    - Interactividad y claridad en la visualización de datos.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

8. <span id="_Toc52661353" class="anchor"></span>**Precedencia y Prioridad**

    - Extracción y clasificación de enlaces.
    - Obtención de métricas.
    - Visualización de resultados.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

9. <span id="_Toc52661354" class="anchor"></span>**Otros requerimientos del producto**

    - Cumplimiento de estándares legales y de privacidad de datos.
    - Uso de buenas prácticas de desarrollo y documentación.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<span id="_Toc52661355" class="anchor"></span>**CONCLUSIONES**

    El sistema propuesto permitirá analizar de manera eficiente el uso de redes sociales en grupos de Telegram, aportando valor académico y facilitando la toma de decisiones basada en datos.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<span id="_Toc52661356" class="anchor"></span>**RECOMENDACIONES**

    - Ampliar el análisis a múltiples grupos y tipos de contenido.
    - Implementar actualizaciones automáticas de datos.
    - Considerar el análisis de sentimiento en futuras versiones.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<span id="_Toc52661357" class="anchor"></span>**BIBLIOGRAFIA**

    - Documentación oficial de Telethon, Power BI, PostgreSQL.
    - Artículos académicos sobre análisis de redes sociales.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<span id="_Toc52661358" class="anchor"></span>**WEBGRAFIA**

    - https://docs.telethon.dev/
    - https://powerbi.microsoft.com/
    - https://www.postgresql.org/
