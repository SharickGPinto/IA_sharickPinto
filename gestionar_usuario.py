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

# --- CAPA DE INTERFAZ (UI) ---
repo = UsuarioRepository(NOMBRE_ARCHIVO)

def _solicitar_tipo_usuario() -> str:
    op = validar_menu("Seleccione el tipo de usuario:\n1. Residente\n2. Administrador\n", 1, 2)
    return transformar_tipo(op)

def imprimir_perfil_usuario(u: Dict):
    print(f"""
    ****************************
    ID:             {u.get('id')}
    NOMBRE:         {u.get('nombre')} {u.get('apellido')}
    TELÉFONO:       {u.get('telefono')}
    DIRECCIÓN:      {u.get('direccion')}
    TIPO:           {u.get('tipo', 'No definido')}
    ****************************""")

def guardar_usuario_ui():
    nuevo_usuario = {
        'nombre':    validar_texto('Ingrese el nombre: ', 1, 30),
        'apellido':  validar_texto('Ingrese el apellido: ', 1, 30),
        'telefono':  validar_entero('Ingrese el número de teléfono: '),
        'direccion': validar_texto('Ingrese la dirección: ', 1, 50),
        'tipo':      _solicitar_tipo_usuario()
    }
    repo.guardar_nuevo(nuevo_usuario)
    print('¡USUARIO GUARDADO CORRECTAMENTE!')

def listar_usuarios_ui():
    registros = repo.obtener_todos()
    if not registros:
        print("No hay usuarios registrados.")
        return
    for u in registros:
        imprimir_perfil_usuario(u)

def buscar_usuario_ui():
    id_buscado = validar_entero("Ingrese el ID a buscar: ")
    usuario = repo.buscar_por_id(id_buscado)
    if usuario:
        imprimir_perfil_usuario(usuario)
    else:
        print(f"No se encontró el usuario con ID: {id_buscado}")

def actualizar_usuario_ui():
    listar_usuarios_ui()
    id_act = validar_entero("Ingrese el ID a actualizar: ")
    
    if not repo.buscar_por_id(id_act):
        print("Usuario no encontrado.")
        return

    opcion = validar_menu("""
    1. Nombre       2. Apellido
    3. Teléfono     4. Dirección
    5. Tipo         6. Cancelar
    Seleccione: """, 1, 6)

    if opcion == 6: return

    cambios = {}
    if opcion == 1: cambios['nombre'] = validar_texto('Nuevo nombre: ', 1, 20)
    elif opcion == 2: cambios['apellido'] = validar_texto('Nuevo apellido: ', 1, 20)
    elif opcion == 3: cambios['telefono'] = validar_entero('Nuevo teléfono: ')
    elif opcion == 4: cambios['direccion'] = validar_texto('Nueva dirección: ', 1, 50)
    elif opcion == 5: cambios['tipo'] = _solicitar_tipo_usuario()

    if repo.actualizar(id_act, cambios):
        print("¡Dato actualizado con éxito!")

def eliminar_usuario_ui():
    listar_usuarios_ui()
    id_elim = validar_entero("Ingrese el ID a eliminar: ")
    nombre_eliminado = repo.eliminar(id_elim)
    
    if nombre_eliminado:
        print(f"El usuario '{nombre_eliminado}' ha sido eliminado.")
    else:
        print("ID no encontrado.")