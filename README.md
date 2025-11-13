# 📸 VisageVault - Gestor de Fotografías Inteligente

## Visión General

**VisageVault** es un gestor de colecciones fotográficas avanzado, diseñado para el entorno Linux (y portable a Windows/macOS), que utiliza la inteligencia artificial para automatizar la organización, la búsqueda y la gestión de metadatos.

En esta fase de desarrollo (v0.1), la aplicación se centra en la estabilidad, la gestión de archivos en colecciones masivas y la edición persistente de metadatos de tiempo.

---

🚀 Funcionalidades Clave de VisageVault (v0.1 Pre-Release)

La aplicación ya no es solo un prototipo, sino una herramienta funcional con gestión avanzada de datos.

1. Gestión de Datos y Persistencia (Backend)

    Persistencia de Datos (SQLite): Utiliza una base de datos local (visagevault.db) como fuente principal de verdad para el año y mes de cada fotografía, garantizando que las ediciones sean permanentes.

    Seguridad Multihilo: La clase VisageVaultDB gestiona las conexiones de SQLite de forma segura (_get_connection), eliminando los errores de RuntimeError al acceder a la base de datos desde el hilo de escaneo.

    Escaneo Inteligente: El PhotoFinderWorker solo calcula la fecha de la foto (EXIF/Modificación) para los archivos nuevos; para los archivos existentes, carga la fecha desde la BD, optimizando drásticamente los tiempos de escaneo.

    Detección de Archivos: Escaneo recursivo de directorios para encontrar archivos con extensiones de imagen comunes (.jpg, .png, etc.).

2. Interfaz de Usuario y Experiencia (Frontend)

    Organización Avanzada: Agrupación dinámica de las fotos en la vista principal por Año y Mes (ej. "2025" -> "Noviembre").

    Navegación Jerárquica: Índice lateral navegable (usando QTreeWidget) que permite saltar instantáneamente a un año o mes específico.

    Visualización Fluida: Implementación de precarga asíncrona de miniaturas (ThumbnailLoader) que asegura que el scroll sea suave y que la interfaz de usuario nunca se congele durante la carga de imágenes.

    Gestión de Espacio: El divisor (QSplitter) permite al usuario ajustar el tamaño de la cuadrícula de fotos y la barra lateral de navegación a su gusto.

3. Visor de Detalles y Edición

    Edición Persistente de Fecha: El diálogo de detalles permite modificar el Año y el Mes mediante campos dedicados. Estos cambios se guardan en la BD y fuerzan la reubicación de la foto en la cuadrícula principal.

    Zoom Interactivo: El ZoomableClickableLabel permite hacer zoom in/out con la rueda del ratón en la foto a tamaño completo.

    Actualización Instantánea: Al guardar una fecha, la señal metadata_changed dispara la reconstrucción de la vista principal, moviendo la foto a su nueva ubicación sin necesidad de escanear el disco de nuevo.

    Visualización de Metadatos: Muestra todos los metadatos EXIF disponibles en un formato de tabla.

📘 Módulos Clave Implementados

Módulo	                 Función Principal
visagevault.py	         Controla la GUI (VisageVaultApp), gestiona hilos y coordina la actualización del modelo de datos.
db_manager.py	         Gestiona la base de datos SQLite, asegura la integridad de los datos (year, month, filepath) y maneja conexiones seguras entre hilos.
photo_finder.py	         Escaneo recursivo de archivos en el disco duro.
metadata_reader.py	     Calcula el año/mes inicial de una foto (usando EXIF o fecha de modificación) y gestiona la lectura/escritura de metadatos EXIF.
thumbnail_generator.py	 Crea y gestiona la caché local de miniaturas.

---

## 💻 Requisitos del Sistema

* **Sistema Operativo:** Linux (Probado en Bash/Desktop Environment).
* **Python:** Versión 3.9 o superior.
* **Hardware:** Se recomienda al menos 4 GB de RAM para el procesamiento de imágenes.

### Instalación de Dependencias

Se requiere un entorno virtual (`venv`) para aislar las dependencias del sistema:

```bash
# Crear y activar el entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar las librerías principales
pip install PySide6 Pillow piexif


### Instalación de Dependencias


## 📜 Licencia

Este proyecto se ofrece bajo un modelo de Doble Licencia (Dual License), brindando máxima flexibilidad:

1. Licencia Pública (LGPLv3)

Este software está disponible bajo la GNU Lesser General Public License v3.0 (LGPLv3).
Puedes usarlo libremente de acuerdo con los términos de la LGPLv3, lo cual es ideal para proyectos de código abierto. En resumen, esto significa que si usas esta biblioteca (especialmente si la modificas), debes cumplir con las obligaciones de la LGPLv3, como publicar el código fuente de tus modificaciones a esta biblioteca y permitir que los usuarios la reemplacen.
Puedes encontrar el texto completo de la licencia en el archivo LICENSE de este repositorio.

2. Licencia Comercial (Privativa)

Si los términos de la LGPLv3 no se ajustan a tus necesidades, ofrezco una licencia comercial alternativa.
Necesitarás una licencia comercial si, por ejemplo:

    Deseas incluir el código en un software propietario (código cerrado) sin tener que publicar tus modificaciones.
    Necesitas enlazar estáticamente (static linking) la biblioteca con tu aplicación propietaria.
    Prefieres no estar sujeto a las obligaciones y restricciones de la LGPLv3.

La licencia comercial te otorga el derecho a usar el código en tus aplicaciones comerciales de código cerrado sin las restricciones de la LGPLv3, a cambio de una tarifa.
Para adquirir una licencia comercial o para más información, por favor, pónte en contacto conmigo en:

dani.eus79@gmail.com


## ✉️ Contacto

Creado por **Daniel Serrano Armenta**

* `dani.eus79@gmail.com`
* Encuéntrame en GitHub: `@danitxu79`
* Portafolio: `https://danitxu79.github.io/`
