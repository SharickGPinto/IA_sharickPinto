from typing import List, Dict
from gestionar_json import cargar, guardar, generar_id

NOMBRE_ARCHIVO = 'herramientas.json'

# --- CRUD BASE ---

def obtener_herramientas() -> List[Dict]:
    return cargar(NOMBRE_ARCHIVO)


def guardar_herramientas(lista: List[Dict]) -> None:
    guardar(NOMBRE_ARCHIVO, lista)


def crear_herramienta(nombre: str, id_categoria: int) -> Dict:
    herramientas = obtener_herramientas()

    nueva = {
        "id": generar_id(herramientas),
        "nombre": nombre,
        "id_categoria": id_categoria,
        "estado": "Disponible"
    }

    herramientas.append(nueva)
    guardar_herramientas(herramientas)

    return nueva


# --- FUNCIONES QUE USA PRESTAMOS (🔥 LAS IMPORTANTES) ---

def listar_herramienta():
    herramientas = obtener_herramientas()

    if not herramientas:
        print("No hay herramientas registradas.")
        return

    print("\n--- LISTADO DE HERRAMIENTAS ---")
    print(f"{'ID':<5} | {'NOMBRE':<20} | {'ESTADO':<15}")
    print("-" * 45)

    for h in herramientas:
        print(f"{h.get('id'):<5} | {h.get('nombre'):<20} | {h.get('estado', 'Disponible')}")


def validar_herramienta(id_herramienta: int):
    herramientas = obtener_herramientas()

    for h in herramientas:
        if h.get('id') == id_herramienta:
            return h

    return False


# --- FUNCIONES EXTRA (OPCIONAL PERO PRO) ---

def eliminar_herramienta(id_herramienta: int) -> bool:
    herramientas = obtener_herramientas()
    nuevas = [h for h in herramientas if h.get('id') != id_herramienta]

    if len(nuevas) == len(herramientas):
        return False

    guardar_herramientas(nuevas)
    return True


def actualizar_herramienta(id_herramienta: int, nuevo_nombre: str = None, nuevo_estado: str = None) -> bool:
    herramientas = obtener_herramientas()

    for h in herramientas:
        if h.get('id') == id_herramienta:
            if nuevo_nombre:
                h['nombre'] = nuevo_nombre
            if nuevo_estado:
                h['estado'] = nuevo_estado

            guardar_herramientas(herramientas)
            return True

    return False