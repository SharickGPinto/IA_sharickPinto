import json
import os
from typing import List, Dict, Any, Union

def cargar(nombre_archivo: str) -> List[Dict[str, Any]]:
    """
    Carga datos desde un archivo JSON. 
    Maneja archivos inexistentes, corruptos o vacíos.
    """
    if not os.path.exists(nombre_archivo):
        return []

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            # Si el archivo está vacío, json.load lanzaría un error
            contenido = archivo.read().strip()
            if not contenido:
                return []
            return json.loads(contenido)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error crítico al leer {nombre_archivo}: {e}")
        return []

def guardar(nombre_archivo: str, lista_datos: List[Dict[str, Any]]) -> bool:
    """
    Guarda la lista de datos en un archivo JSON con formato legible.
    Retorna True si la operación fue exitosa.
    """
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(lista_datos, archivo, indent=4, ensure_ascii=False)
        return True
    except IOError as e:
        print(f"Error al escribir en el archivo {nombre_archivo}: {e}")
        return False

def generar_id(datos: List[Dict[str, Any]]) -> int:
    """
    Genera un ID incremental basado en el valor más alto actual.
    Garantiza que el ID sea siempre un entero.
    """
    if not datos:
        return 1
    
    # Buscamos el ID máximo de forma segura, ignorando registros mal formados
    ids = [item.get('id') for item in datos if isinstance(item.get('id'), int)]
    
    return max(ids) + 1 if ids else 1