import os
from typing import Optional

def cargar_txt(nombre_archivo: str) -> str:
    """
    Lee el contenido completo de un archivo de texto de forma segura.
    Retorna una cadena vacía si el archivo no existe.
    """
    if not os.path.exists(nombre_archivo):
        return ""

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            return archivo.read()
    except (IOError, UnicodeDecodeError) as e:
        print(f"Error al leer el archivo {nombre_archivo}: {e}")
        return ""

def guardar_txt(nombre_archivo: str, mensaje: str, modo: str = 'a') -> bool:
    """
    Escribe o añade un mensaje a un archivo de texto.
    
    Args:
        nombre_archivo: Ruta del archivo.
        mensaje: Texto a escribir.
        modo: 'a' para añadir al final (logs), 'w' para sobreescribir (reportes).
    """
    try:
        # Aseguramos que el directorio exista (opcional pero recomendado)
        with open(nombre_archivo, modo, encoding="utf-8") as archivo:
            archivo.write(f"{mensaje}\n")
        return True
    except IOError as e:
        print(f"Error de escritura en {nombre_archivo}: {e}")
        return False

def limpiar_archivo_txt(nombre_archivo: str):
    """Limpia el contenido del archivo sin borrarlo."""
    guardar_txt(nombre_archivo, "", modo='w')