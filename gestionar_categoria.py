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


# --- CAPA DE INTERFAZ DE USUARIO (CONTROLADOR DE CONSOLA) ---
repo = CategoriaRepository(NOMBRE_ARCHIVO)

def guardar_categoria_ui():  # Corregido: antes era crear_categoria_ui
    nombre = validar_texto('Ingrese el nombre de la categoría: ', 1, 30)
    repo.guardar_nueva(nombre)
    print('¡Categoría guardada exitosamente!')

def listar_categorias_ui():
    registros = repo.obtener_todas()
    if not registros:
        print("No hay categorías registradas.")
        return

    print("\n--- LISTADO DE CATEGORÍAS ---")
    for cat in registros:
        print(f"ID: {cat['id']:<5} | Categoría: {cat['nombre']}")

def buscar_categoria_ui():
    id_buscar = validar_entero("Ingrese el ID a buscar: ")
    categoria = repo.buscar_por_id(id_buscar)
    
    if categoria:
        print(f"\nResultado:\nID: {categoria['id']}\nNombre: {categoria['nombre']}")
    else:
        print(f"Error: No se encontró la categoría con ID {id_buscar}")

def actualizar_categoria_ui():
    listar_categorias_ui()
    id_actualizar = validar_entero("Ingrese el ID a modificar: ")
    
    if not repo.buscar_por_id(id_actualizar):
        print("ID no encontrado.")
        return

    opcion = validar_menu("1. Editar Nombre\n2. Cancelar\nSeleccione: ", 1, 2)
    if opcion == 1:
        nuevo_nombre = validar_texto("Nuevo nombre: ", 1, 20)
        if repo.actualizar(id_actualizar, nuevo_nombre):
            print("¡Registro actualizado!")
    else:
        print("Operación cancelada.")

def eliminar_categoria_ui():
    listar_categorias_ui()
    id_eliminar = validar_entero("Ingrese el ID a eliminar: ")
    
    if repo.eliminar(id_eliminar):
        print(f"Categoría {id_eliminar} eliminada correctamente.")
    else:
        print("No se pudo eliminar: ID no encontrado.")