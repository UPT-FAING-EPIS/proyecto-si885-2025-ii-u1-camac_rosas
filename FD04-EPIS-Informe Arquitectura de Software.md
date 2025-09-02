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

**Documento de Arquitectura de Software**

**Versión *1.0***

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

|CONTROL DE VERSIONES||||||
| :-: | :- | :- | :- | :- | :- |
|Versión|Hecha por|Revisada por|Aprobada por|Fecha|Motivo|
|1\.0|MPV|ELV|ARV|10/10/2020|Versión Original|

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

**INDICE GENERAL**
#
1.  [INTRODUCCIÓN](#introduccion)
    1.1. Propósito (Diagrama 4+1)
    1.2. Alcance
    1.3. Definición, siglas y abreviaturas
    1.4. Organización del documento
2.  [OBJETIVOS Y RESTRICCIONES ARQUITECTONICAS](#objetivos-y-restricciones)
    2.1.1. Requerimientos Funcionales
    2.1.2. Requerimientos No Funcionales – Atributos de Calidad
3.  [REPRESENTACIÓN DE LA ARQUITECTURA DEL SISTEMA](#representacion-arquitectura)
    3.1. Vista de Caso de uso
    3.1.1. Diagramas de Casos de uso
    3.2. Vista Lógica
    3.2.1. Diagrama de Subsistemas (paquetes)
    3.2.2. Diagrama de Secuencia (vista de diseño)
    3.2.3. Diagrama de Colaboración (vista de diseño)
    3.2.4. Diagrama de Objetos
    3.2.5. Diagrama de Clases
    3.2.6. Diagrama de Base de datos (relacional o no relacional)
    3.3. Vista de Implementación (vista de desarrollo)
    3.3.1. Diagrama de arquitectura software (paquetes)
    3.3.2. Diagrama de arquitectura del sistema (Diagrama de componentes)
    3.4. Vista de procesos
    3.4.1. Diagrama de Procesos del sistema (diagrama de actividad)
    3.5. Vista de Despliegue (vista física)
    3.5.1. Diagrama de despliegue
4.  [ATRIBUTOS DE CALIDAD DEL SOFTWARE](#atributos-de-calidad)
    Escenario de Funcionalidad
    Escenario de Usabilidad
    Escenario de confiabilidad
    Escenario de rendimiento
    Escenario de mantenibilidad
    Otros Escenarios

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## <a name="introduccion"></a>1. INTRODUCCIÓN

### 1.1. Propósito (Diagrama 4+1)
Este documento presenta una visión global y resumida de la arquitectura del proyecto “Análisis de Uso de Redes Sociales en Grupos de Telegram”. Describe cómo los requerimientos funcionales y no funcionales influyen en el diseño, definiendo las prioridades y decisiones clave.

### 1.2. Alcance
Este documento se centrará en el desarrollo de la vista lógica del sistema. Incluirá aspectos fundamentales de las otras vistas arquitectónicas, omitiendo detalles no pertinentes para una visión general.

### 1.3. Definición, siglas y abreviaturas
Este apartado proporciona las definiciones de los términos, acrónimos y abreviaturas clave utilizados en el documento.
* **API**: Interfaz de programación de aplicaciones.
* **Dashboard**: Panel interactivo de visualización de datos.
* **Power BI**: Herramienta de visualización de datos de Microsoft.
* **PostgreSQL**: Sistema de gestión de bases de datos relacional.
* **SRS**: Especificación de Requerimientos de Software (por sus siglas en inglés, Software Requirements Specification).
* **Telegram**: Plataforma de mensajería instantánea.

### 1.4. Organización del documento
El documento se organiza en secciones que cubren los objetivos y restricciones, la representación de la arquitectura a través del modelo 4+1 de vistas y, finalmente, un análisis de los atributos de calidad del software.

---

## <a name="objetivos-y-restricciones"></a>2. OBJETIVOS Y RESTRICCIONES ARQUITECTONICAS

### Priorización de requerimientos
Se establecen las prioridades de los requerimientos y las restricciones del proyecto para definir el orden de implementación.

### 2.1.1. Requerimientos Funcionales
| ID | Descripción | Prioridad |
| :--: | :--- | :---: |
| RF01 | El sistema debe extraer automáticamente mensajes con enlaces desde Telegram. | Alta |
| RF02 | El sistema debe clasificar los enlaces por red social (Facebook, Instagram, TikTok, etc.). | Alta |
| RF03 | El sistema debe obtener métricas de interacción (likes, comentarios, fecha). | Media |
| RF04 | El sistema debe identificar y clasificar a los usuarios más activos. | Media |
| RF05 | El sistema debe almacenar los datos extraídos en una base de datos relacional. | Alta |
| RF06 | El sistema debe generar un conjunto de datos compatible con Power BI. | Alta |
| RF07 | El sistema debe visualizar los resultados en dashboards interactivos. | Alta |

### 2.1.2. Requerimientos No Funcionales – Atributos de Calidad
| ID | Descripción | Prioridad |
| :--: | :--- | :---: |
| RNF01 | **Rendimiento:** El sistema debe procesar un volumen de 1000 mensajes con enlaces en menos de 5 minutos. | Media |
| RNF02 | **Usabilidad:** Los dashboards de Power BI deben ser intuitivos y fáciles de usar para los usuarios analistas. | Alta |
| RNF03 | **Fiabilidad:** La extracción y clasificación de enlaces debe tener una precisión superior al 95%. | Alta |
| RNF04 | **Seguridad:** El sistema debe manejar las credenciales de acceso a Telegram y APIs de manera segura. | Alta |
| RNF05 | **Escalabilidad:** El sistema debe ser capaz de procesar más de un grupo de Telegram simultáneamente en futuras versiones. | Baja |

---

## <a name="representacion-arquitectura"></a>3. REPRESENTACIÓN DE LA ARQUITECTURA DEL SISTEMA

### 3.1. Vista de Caso de uso
Esta sección describe los casos de uso principales y los actores que interactúan con el sistema.

### 3.1.1. Diagramas de Casos de uso
La estructura del sistema se ilustra a través de los siguientes escenarios de casos de uso:
* **Analizar datos de Telegram**: El usuario accede al dashboard en Power BI para visualizar los datos procesados por el sistema.
* **Extraer enlaces de un grupo**: El desarrollador ejecuta el script para obtener mensajes de un grupo de Telegram.

### 3.2. Vista Lógica
Esta vista representa los requerimientos funcionales del sistema, organizados en subsistemas y paquetes.

### 3.2.1. Diagrama de Subsistemas (paquetes)
* `com.upt.project.extraction`: Módulo para la extracción de datos de Telegram.
* `com.upt.project.processing`: Módulo para la clasificación de enlaces y obtención de métricas.
* `com.upt.project.database`: Módulo para la gestión de la base de datos PostgreSQL.
* `com.upt.project.visualization`: Módulo para la visualización de datos en Power BI.

### 3.2.2. Diagrama de Secuencia (vista de diseño)
(Este diagrama visualiza la interacción entre los objetos)
1.  **Script de Extracción** se comunica con la **Telegram API** para `getMessages()`.
2.  La **Telegram API** devuelve los **[Mensajes]** al **Script de Extracción**.
3.  El **Script de Extracción** envía los mensajes al **Procesador** para `processLinks()`.
4.  El **Procesador** se comunica con la **Red Social API** para `getMetrics()`.
5.  La **Red Social API** devuelve las **[Métricas]** al **Procesador**.
6.  El **Procesador** envía los datos a la **BD_PostgreSQL** para `saveData()`.

### 3.2.3. Diagrama de Colaboración (vista de diseño)
No aplica en este nivel de detalle.

### 3.2.4. Diagrama de Objetos
* **Mensaje**: Contiene atributos como `id_mensaje`, `autor_id` y `contenido`.
* **Enlace**: Contiene `url`, `red_social`, `likes` y `comentarios`.

### 3.2.5. Diagrama de Clases
(Este diagrama visualiza la estructura estática de las clases y sus relaciones)
* **Clase `Mensaje`**: id_mensaje, autor_id, fecha, contenido.
* **Clase `Enlace`**: url, red_social, likes, comentarios, fecha_publicacion.
* **Clase `Usuario`**: id_usuario, nombre.
* **Relaciones**: Un `Usuario` "Comparte" un `Mensaje`. Un `Mensaje` "Contiene" un `Enlace`.

### 3.2.6. Diagrama de Base de datos (relacional o no relacional)
El sistema utilizará una base de datos relacional **PostgreSQL** para almacenar los datos extraídos.

### 3.3. Vista de Implementación (vista de desarrollo)
Esta vista detalla la estructura del modelo de implementación.

### 3.3.1. Diagrama de arquitectura software (paquetes)
El sistema está diseñado en una arquitectura de capas:
* **Capa de Extracción**: Maneja la conexión con la API de Telegram.
* **Capa de Negocio/Procesamiento**: Clasifica y enriquece los datos.
* **Capa de Persistencia**: Interactúa con la base de datos PostgreSQL.
* **Capa de Presentación**: Los dashboards de Power BI que visualizan los datos.

### 3.3.2. Diagrama de arquitectura del sistema (Diagrama de componentes)
(Este diagrama visualiza la interconexión entre los componentes)
* **Componente Extractor**: Un script de Python que se conecta a Telegram.
* **Componente Procesador**: Un script de Python que limpia y clasifica los datos.
* **Componente Base de Datos**: PostgreSQL, que almacena los datos.
* **Componente de Visualización**: El archivo de Power BI que se conecta a la base de datos.

### 3.4. Vista de procesos
Esta vista describe la descomposición del sistema en procesos.

### 3.4.1. Diagrama de Procesos del sistema (diagrama de actividad)
* **Actividad 1: Extracción**: El sistema se conecta al grupo de Telegram.
* **Actividad 2: Procesamiento**: Los enlaces se analizan y clasifican.
* **Actividad 3: Carga**: Los datos se insertan en la base de datos.
* **Actividad 4: Visualización**: Power BI actualiza los dashboards.

### 3.5. Vista de Despliegue (vista física)
Esta vista describe la distribución física del sistema.

### 3.5.1. Diagrama de despliegue
(Este diagrama visualiza los nodos y componentes)
* **Nodo `Computadora del Desarrollador`**: Aloja los scripts de Python y la base de datos PostgreSQL.
* **Nodo `Servicio de Power BI`**: Se conecta remotamente a la base de datos para la visualización.
* **Nodo `Servidores de Telegram`**: Proporcionan la API para la extracción de datos.

---

## <a name="atributos-de-calidad"></a>4. ATRIBUTOS DE CALIDAD DEL SOFTWARE

### Escenario de Funcionalidad
El sistema debe ser capaz de procesar **todos los tipos de enlaces de redes sociales** definidos en el alcance y extraer las métricas correspondientes, asegurando la integridad de los datos extraídos.

### Escenario de Usabilidad
Los **dashboards de Power BI** deben ser lo suficientemente intuitivos para que un **analista de datos no técnico** pueda navegar, filtrar la información y generar reportes sin necesidad de asistencia, logrando una **utilización eficiente del sistema**.

### Escenario de confiabilidad
El sistema debe garantizar la **integridad de la información** y la **disponibilidad de los datos**. Por ejemplo, si una extracción falla, el sistema debe ser capaz de reanudar el proceso y evitar la pérdida de datos ya procesados.

### Escenario de rendimiento
El sistema debe **procesar 1000 mensajes con enlaces en menos de 5 minutos** para asegurar un tiempo de respuesta rápido y eficiente, incluso con volúmenes de datos significativos.

### Escenario de mantenibilidad
El código debe estar bien documentado y organizado en paquetes claros (`.extraction`, `.processing`, etc.) para que un nuevo desarrollador pueda **entender y adaptar el sistema** fácilmente, permitiendo la **ampliación del análisis a nuevos grupos o redes sociales**.

### Otros Escenarios
**Performance**: El sistema debe garantizar que el tiempo requerido para responder a los eventos de extracción y visualización sea mínimo, permitiendo que los dashboards se actualicen en un tiempo aceptable para el usuario final.
