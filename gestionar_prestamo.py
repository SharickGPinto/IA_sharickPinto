from typing import List, Dict, Optional
from datetime import timedelta
from gestionar_json import cargar, guardar, generar_id
from gestionar_usuario import listar_usuario, validar_usuario
from gestionar_herramienta import listar_herramienta, validar_herramienta
from validaciones import validar_entero, validar_menu
from transformaciones import solicitar_fecha_inicio, gestionar, rechazar

NOMBRE_ARCHIVO = 'prestamos.json'

# --- REPOSITORIO ---
class PrestamoRepository:
    def __init__(self, archivo: str):
        self.archivo = archivo

    def obtener_todos(self) -> List[Dict]:
        return cargar(self.archivo)

    def guardar_nuevo(self, datos: Dict) -> int:
        registros = self.obtener_todos()
        nuevo_id = generar_id(registros)
        datos['id'] = nuevo_id
        registros.append(datos)
        guardar(self.archivo, registros)
        return nuevo_id

    def buscar_por_id(self, prestamo_id: int) -> Optional[Dict]:
        registros = self.obtener_todos()
        return next((p for p in registros if p.get('id') == prestamo_id), None)

    def actualizar_registros(self, registros_actualizados: List[Dict]):
        guardar(self.archivo, registros_actualizados)

    def eliminar(self, prestamo_id: int) -> bool:
        registros = self.obtener_todos()
        nuevos = [p for p in registros if p.get('id') != prestamo_id]
        if len(nuevos) < len(registros):
            self.actualizar_registros(nuevos)
            return True
        return False

repo = PrestamoRepository(NOMBRE_ARCHIVO)

# --- UTILIDAD ---
def imprimir_ticket_prestamo(p: Dict):
    usuario = p.get('usuario', {})
    herramienta = p.get('herramienta', {})

    print(f"""
=========================================
ID: {p.get('id')}
Estado: {p.get('estado')}
Usuario: {usuario.get('nombre')} (ID {usuario.get('id')})
Herramienta: {herramienta.get('nombre')} (ID {herramienta.get('id')})
Cantidad: {p.get('cantidad')}
Inicio: {p.get('fecha_inicio')}
Fin: {p.get('fecha_final')}
Observaciones: {p.get('observaciones')}
=========================================
""")

def _validar_entidad_ui(nombre, listar, validar):
    listar()
    while True:
        id_val = validar_entero(f"ID {nombre}: ")
        data = validar(id_val)
        if data:
            return data
        print("No existe.")

# --- FUNCIONES UI (🔥 TODAS LAS NECESARIAS) ---

def guardar_prestamo_ui():
    usuario = _validar_entidad_ui('usuario', listar_usuario, validar_usuario)
    herramienta = _validar_entidad_ui('herramienta', listar_herramienta, validar_herramienta)

    cantidad = validar_entero("Cantidad: ")
    fecha_inicio = solicitar_fecha_inicio()
    dias = validar_entero("Días: ")
    fecha_final = fecha_inicio + timedelta(days=dias)

    nuevo = {
        "usuario": usuario,
        "herramienta": herramienta,
        "cantidad": cantidad,
        "fecha_inicio": str(fecha_inicio),
        "fecha_final": str(fecha_final),
        "estado": "En proceso",
        "observaciones": "Pendiente"
    }

    id_gen = repo.guardar_nuevo(nuevo)
    print(f"Préstamo creado con ID: {id_gen}")

# 🔥 ESTA TE FALTABA
def buscar_prestamo_ui():
    id_buscar = validar_entero("ID préstamo: ")
    p = repo.buscar_por_id(id_buscar)

    if p:
        imprimir_ticket_prestamo(p)
    else:
        print("No encontrado.")

def consultar_prestamos_ui():
    registros = repo.obtener_todos()

    if not registros:
        print("No hay préstamos.")
        return

    for p in registros:
        imprimir_ticket_prestamo(p)

def gestionar_prestamo_ui():
    consultar_prestamos_ui()
    id_gestion = validar_entero("ID a gestionar: ")
    registros = repo.obtener_todos()

    for p in registros:
        if p.get('id') == id_gestion:
            op = validar_menu("1. Aprobar\n2. Rechazar\n>>> ", 1, 2)

            if op == 1:
                gestionar(p.get('herramienta', {}).get('id'), p)
            else:
                rechazar(p)

            repo.actualizar_registros(registros)
            print("Actualizado.")
            return

    print("No encontrado.")

def eliminar_prestamo_ui():
    id_elim = validar_entero("ID a eliminar: ")

    if repo.eliminar(id_elim):
        print("Eliminado.")
    else:
        print("No existe.")