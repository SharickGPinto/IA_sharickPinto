from typing import List, Dict, Optional, Any
from gestionar_json import cargar, guardar, generar_id
from validaciones import validar_entero, validar_texto, validar_menu
from transformaciones import transformar_tipo

NOMBRE_ARCHIVO = 'usuarios.json'

# --- CAPA DE LÓGICA (REPOSITORIO) ---
class UsuarioRepository:
    def __init__(self, archivo: str):
        self.archivo = archivo

    def obtener_todos(self) -> List[Dict]:
        return cargar(self.archivo)

    def guardar_nuevo(self, datos: Dict) -> None:
        registros = self.obtener_todos()
        datos['id'] = generar_id(registros)
        registros.append(datos)
        guardar(self.archivo, registros)

    def buscar_por_id(self, usuario_id: int) -> Optional[Dict]:
        registros = self.obtener_todos()
        return next((u for u in registros if u.get('id') == usuario_id), None)

    def actualizar(self, usuario_id: int, nuevos_datos: Dict) -> bool:
        registros = self.obtener_todos()
        for u in registros:
            if u.get('id') == usuario_id:
                u.update(nuevos_datos)
                guardar(self.archivo, registros)
                return True
        return False

    def eliminar(self, usuario_id: int) -> Optional[str]:
        registros = self.obtener_todos()
        for u in registros:
            if u.get('id') == usuario_id:
                nombre = u.get('nombre')
                registros.remove(u)
                guardar(self.archivo, registros)
                return nombre
        return None

# Instancia global para los métodos internos
repo = UsuarioRepository(NOMBRE_ARCHIVO)

# --- FUNCIONES QUE PIDE EL MÓDULO DE PRÉSTAMOS (IMPORTANTE) ---

def listar_usuario():
    """Función puente para gestionar_prestamo.py"""
    registros = repo.obtener_todos()
    if not registros:
        print("No hay usuarios registrados.")
        return
    for u in registros:
        print(f"ID: {u.get('id')} | Nombre: {u.get('nombre')} {u.get('apellido')}")

def validar_usuario(usuario_id: int):
    """Función puente para gestionar_prestamo.py"""
    usuario = repo.buscar_por_id(usuario_id)
    return usuario if usuario else False

# --- CAPA DE INTERFAZ DE USUARIO (UI) ---

def guardar_usuario_ui():
    print("\n--- REGISTRO DE USUARIO ---")
    nuevo = {
        'nombre':    validar_texto('Nombre: ', 1, 30),
        'apellido':  validar_texto('Apellido: ', 1, 30),
        'telefono':  validar_entero('Teléfono: '),
        'direccion': validar_texto('Dirección: ', 1, 50),
        'tipo':      transformar_tipo(validar_menu("1. Residente\n2. Admin\n", 1, 2))
    }
    repo.guardar_nuevo(nuevo)
    print('¡Usuario registrado!')

def listar_usuarios_ui():
    print("\n--- LISTADO GENERAL ---")
    listar_usuario()

def buscar_usuario_ui():
    id_buscado = validar_entero("ID a buscar: ")
    u = repo.buscar_por_id(id_buscado)
    if u:
        print(f"ID: {u['id']} | {u['nombre']} {u['apellido']} | {u['tipo']}")
    else:
        print("No encontrado.")

def actualizar_usuario_ui():
    listar_usuarios_ui()
    id_act = validar_entero("ID a modificar: ")
    if repo.buscar_por_id(id_act):
        # Lógica simplificada para el ejemplo
        nuevo_nom = validar_texto("Nuevo nombre: ", 1, 30)
        repo.actualizar(id_act, {'nombre': nuevo_nom})
        print("Actualizado.")

def eliminar_usuario_ui():
    listar_usuarios_ui()
    id_elim = validar_entero("ID a eliminar: ")
    if repo.eliminar(id_elim):
        print("Eliminado con éxito.")