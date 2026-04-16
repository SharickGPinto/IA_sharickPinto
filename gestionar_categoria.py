from typing import List, Optional, Dict, Any
from validaciones import validar_menu, validar_texto, validar_entero
from gestionar_json import cargar, guardar, generar_id

# Configuración constante
NOMBRE_ARCHIVO = 'categorias.json'

# --- CAPA DE LÓGICA DE NEGOCIO (REPOSITORIO) ---
class CategoriaRepository:
    """Maneja la persistencia y reglas de negocio de las categorías."""
    
    def __init__(self, archivo: str):
        self.archivo = archivo

    def obtener_todas(self) -> List[Dict[str, Any]]:
        return cargar(self.archivo)

    def buscar_por_id(self, categoria_id: int) -> Optional[Dict[str, Any]]:
        registros = self.obtener_todas()
        return next((c for c in registros if c.get('id') == categoria_id), None)

    def guardar_nueva(self, nombre: str) -> None:
        registros = self.obtener_todas()
        nueva_categoria = {
            'id': generar_id(registros),
            'nombre': nombre
        }
        registros.append(nueva_categoria)
        guardar(self.archivo, registros)

    def actualizar(self, categoria_id: int, nuevo_nombre: str) -> bool:
        registros = self.obtener_todas()
        for categoria in registros:
            if categoria.get('id') == categoria_id:
                categoria['nombre'] = nuevo_nombre
                guardar(self.archivo, registros)
                return True
        return False

    def eliminar(self, categoria_id: int) -> bool:
        registros = self.obtener_todas()
        original_count = len(registros)
        registros = [c for c in registros if c.get('id') != categoria_id]
        
        if len(registros) < original_count:
            guardar(self.archivo, registros)
            return True
        return False

# Instancia global para ser usada por otros módulos
repo = CategoriaRepository(NOMBRE_ARCHIVO)

# --- FUNCIONES DE COMPATIBILIDAD (Para que gestionar_herramienta no falle) ---

def validar_categoria(id_categoria: int):
    """Retorna la categoría si existe, de lo contrario False."""
    categoria = repo.buscar_por_id(id_categoria)
    return categoria if categoria else False

def listar_categoria():
    """Versión simple de listado para procesos internos."""
    registros = repo.obtener_todas()
    if not registros:
        print("No hay categorías.")
        return
    for c in registros:
        print(f"ID: {c['id']} - {c['nombre']}")

# --- CAPA DE INTERFAZ DE USUARIO (CONTROLADOR DE CONSOLA) ---

def guardar_categoria_ui():
    nombre = validar_texto('Ingrese el nombre de la categoría: ', 1, 30)
    repo.guardar_nueva(nombre)
    print('¡Categoría guardada exitosamente!')

def listar_categorias_ui():
    print("\n--- LISTADO DE CATEGORÍAS ---")
    listar_categoria()

def buscar_categoria_ui():
    id_buscar = validar_entero("Ingrese el ID a buscar: ")
    categoria = repo.buscar_por_id(id_buscar)
    if categoria:
        print(f"\nResultado: ID {categoria['id']} | Nombre: {categoria['nombre']}")
    else:
        print(f"Error: No se encontró el ID {id_buscar}")

def actualizar_categoria_ui():
    listar_categorias_ui()
    id_act = validar_entero("Ingrese el ID a modificar: ")
    if not repo.buscar_por_id(id_act):
        print("ID no encontrado.")
        return
    nuevo_nombre = validar_texto("Nuevo nombre: ", 1, 20)
    if repo.actualizar(id_act, nuevo_nombre):
        print("¡Actualizado!")

def eliminar_categoria_ui():
    listar_categorias_ui()
    id_elim = validar_entero("Ingrese el ID a eliminar: ")
    if repo.eliminar(id_elim):
        print(f"Categoría {id_elim} eliminada.")
    else:
        print("ID no encontrado.")