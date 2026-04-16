from typing import List, Dict, Any, Optional
from gestionar_json import cargar, guardar, generar_id
from validaciones import validar_menu, validar_entero, validar_texto
from gestionar_categoria import validar_categoria, listar_categoria
from transformaciones import transformar_estado

NOMBRE_ARCHIVO = 'herramientas.json'

# --- CAPA DE LÓGICA (REPOSITORIO) ---
class HerramientaRepository:
    def __init__(self, archivo: str):
        self.archivo = archivo

    def obtener_todas(self) -> List[Dict]:
        return cargar(self.archivo)

    def guardar_nueva(self, datos: Dict) -> None:
        registros = self.obtener_todas()
        datos['id'] = generar_id(registros)
        registros.append(datos)
        guardar(self.archivo, registros)

    def actualizar(self, herramienta_id: int, nuevos_datos: Dict) -> bool:
        registros = self.obtener_todas()
        for h in registros:
            if h.get('id') == herramienta_id:
                h.update(nuevos_datos)
                guardar(self.archivo, registros)
                return True
        return False

    def eliminar(self, herramienta_id: int) -> Optional[str]:
        registros = self.obtener_todas()
        for h in registros:
            if h.get('id') == herramienta_id:
                nombre = h.get('nombre')
                registros.remove(h)
                guardar(self.archivo, registros)
                return nombre
        return None

# --- CAPA DE INTERFAZ (UI) ---
repo = HerramientaRepository(NOMBRE_ARCHIVO)

def _solicitar_categoria_valida() -> Dict:
    listar_categoria()
    while True:
        id_cat = validar_entero('Ingrese el ID de la categoría: ')
        categoria = validar_categoria(id_cat)
        if categoria:
            return categoria
        print("Error: Categoría no encontrada.")

def _solicitar_estado_valido() -> str:
    op = validar_menu("1. Activa\n2. Fuera de servicio\n3. Reparación\nSeleccione: ", 1, 3)
    return transformar_estado(op)

def guardar_herramienta_ui():
    nueva = {
        'nombre':   validar_texto('Ingrese el nombre: ', 1, 20),
        'categoria': _solicitar_categoria_valida(),
        'cantidad':  validar_entero('Cantidad disponible: '),
        'estado':    _solicitar_estado_valido(),
        'precio':    validar_entero('Precio de costo: ')
    }
    repo.guardar_nueva(nueva)
    print('¡DATOS GUARDADOS CORRECTAMENTE!')

def listar_herramientas_ui():
    registros = repo.obtener_todas()
    if not registros:
        print("No hay herramientas registradas.")
        return
        
    for h in registros:
        cat = h.get('categoria', {})
        print(f"""
        {'*' * 40}
        ID:         {h.get('id')}
        NOMBRE:     {h.get('nombre')}
        CATEGORÍA:  {cat.get('nombre', 'N/A')} (ID: {cat.get('id')})
        STOCK:      {h.get('cantidad')} | ESTADO: {h.get('estado')}
        PRECIO:     ${h.get('precio'):,.0f}""")

def actualizar_herramienta_ui():
    listar_herramientas_ui()
    id_act = validar_entero("Ingrese el ID a actualizar: ")
    
    opcion = validar_menu("""
        1. Nombre     2. Categoría
        3. Estado     4. Precio
        5. Cantidad   6. Cancelar
        Seleccione: """, 1, 6)
    
    if opcion == 6: return

    # Mapeo de lógica para evitar match/case gigante
    cambios = {}
    if opcion == 1: cambios['nombre'] = validar_texto('Nuevo nombre: ', 1, 20)
    elif opcion == 2: cambios['categoria'] = _solicitar_categoria_valida()
    elif opcion == 3: cambios['estado'] = _solicitar_estado_valido()
    elif opcion == 4: cambios['precio'] = validar_entero('Nuevo precio: ')
    elif opcion == 5: cambios['cantidad'] = validar_entero('Nueva cantidad: ')

    if repo.actualizar(id_act, cambios):
        print("¡Dato actualizado con éxito!")
    else:
        print(f"No se encontró el ID {id_act}")

def eliminar_herramienta_ui():
    listar_herramientas_ui()
    id_elim = validar_entero("Ingrese el ID a eliminar: ")
    nombre_eliminado = repo.eliminar(id_elim)
    
    if nombre_eliminado:
        print(f"La herramienta '{nombre_eliminado}' ha sido eliminada.")
    else:
        print("ID no encontrado.")