from typing import List, Dict
from gestionar_json import cargar, guardar, generar_id
from validaciones import validar_menu, validar_texto, validar_entero
from gestionar_categoria import validar_categoria, listar_categoria

NOMBRE_ARCHIVO = 'herramientas.json'

# --- LOGICA ---

def obtener_herramientas() -> List[Dict]:
    return cargar(NOMBRE_ARCHIVO)

def guardar_nueva_herramienta(datos: Dict) -> None:
    registros = obtener_herramientas()
    datos['id'] = generar_id(registros)
    registros.append(datos)
    guardar(NOMBRE_ARCHIVO, registros)

# --- FUNCIONES PARA OTROS MODULOS ---

def listar_herramienta():
    registros = obtener_herramientas()
    if not registros:
        print("No hay herramientas.")
        return
    
    for h in registros:
        print(h)

def validar_herramienta(id_herramienta: int):
    registros = obtener_herramientas()
    return next((h for h in registros if h.get('id') == id_herramienta), False)

# --- UI ---

def guardar_herramienta_ui():
    nombre = validar_texto("Nombre: ", 1, 50)
    
    listar_categoria()
    id_cat = validar_entero("ID categoria: ")
    
    if not validar_categoria(id_cat):
        print("Categoria no existe")
        return

    nueva = {
        "nombre": nombre,
        "id_categoria": id_cat,
        "estado": "Disponible"
    }

    guardar_nueva_herramienta(nueva)
    print("Guardado")

def listar_herramientas_ui():
    listar_herramienta()

def menu_herramienta():   # 🔥 ESTA FUNCIÓN ES LA CLAVE
    while True:
        op = validar_menu('''
        1) Registrar
        2) Listar
        3) Volver
        >>> ''', 1, 3)

        match op:
            case 1:
                guardar_herramienta_ui()
            case 2:
                listar_herramientas_ui()
            case 3:
                break