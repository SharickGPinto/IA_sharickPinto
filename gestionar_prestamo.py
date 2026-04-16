from typing import List, Dict, Optional, Any
from datetime import timedelta
from gestionar_json import cargar, guardar, generar_id
from gestionar_usuario import listar_usuario, validar_usuario
from gestionar_herramienta import listar_herramienta, validar_herramienta
from validaciones import validar_entero, validar_menu
from transformaciones import solicitar_fecha_inicio, gestionar, rechazar

NOMBRE_ARCHIVO = 'prestamos.json'

# --- CAPA DE LÓGICA (REPOSITORIO) ---
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
        original_len = len(registros)
        registros = [p for p in registros if p.get('id') != prestamo_id]
        if len(registros) < original_len:
            self.actualizar_registros(registros)
            return True
        return False

# --- CAPA DE INTERFAZ (UI) ---
repo = PrestamoRepository(NOMBRE_ARCHIVO)

def imprimir_ticket_prestamo(p: Dict):
    """Estandarización de salida para evitar duplicación."""
    usuario = p.get('usuario', {})
    herramienta = p.get('herramienta', {})
    print(f"""
    {'='*45}
    ID PRÉSTAMO:    {p.get('id')}
    ESTADO:         [{p.get('estado').upper()}]
    USUARIO:        {usuario.get('nombre')} (ID: {usuario.get('id')})
    HERRAMIENTA:    {herramienta.get('nombre')} (ID: {herramienta.get('id')})
    CANTIDAD:       {p.get('cantidad')}
    FECHAS:         {p.get('fecha_inicio')} --> {p.get('fecha_final')}
    OBSERVACIONES:  {p.get('observaciones')}
    {'='*45}""")

def _validar_entidad_ui(entidad_nombre: str, func_listar, func_validar):
    """Helper para validar usuarios y herramientas genéricamente."""
    func_listar()
    while True:
        id_entidad = validar_entero(f'Ingrese el ID del {entidad_nombre}: ')
        datos = func_validar(id_entidad)
        if datos:
            return datos
        print(f"Error: {entidad_nombre} no encontrado.")

def guardar_prestamo_ui():
    usuario = _validar_entidad_ui('usuario', listar_usuario, validar_usuario)
    herramienta = _validar_entidad_ui('herramienta', listar_herramienta, validar_herramienta)
    
    cantidad = validar_entero('Cantidad de herramientas a solicitar: ')
    fecha_inicio_dt = solicitar_fecha_inicio()
    dias = validar_entero('Días de préstamo: ')
    fecha_final_dt = fecha_inicio_dt + timedelta(days=dias)

    nuevo_prestamo = {
        'usuario': usuario,
        'herramienta': herramienta,
        'cantidad': cantidad,
        'fecha_inicio': str(fecha_inicio_dt),
        'fecha_final': str(fecha_final_dt),
        'estado': 'En proceso',
        'observaciones': 'Pendiente'
    }

    id_generado = repo.guardar_nuevo(nuevo_prestamo)
    print(f'\n¡ÉXITO! ID DE SEGUIMIENTO: {id_generado}')

def consultar_prestamos_ui(por_usuario: bool = False):
    registros = repo.obtener_todos()
    if not registros:
        print("No hay préstamos registrados.")
        return

    filtro_id = None
    if por_usuario:
        filtro_id = validar_entero('Ingrese su ID de Usuario para el historial: ')
    
    encontrado = False
    for p in registros:
        if not por_usuario or p.get('usuario', {}).get('id') == filtro_id:
            imprimir_ticket_prestamo(p)
            encontrado = True
    
    if not encontrado:
        print("No se encontraron registros.")

def gestionar_prestamo_ui():
    consultar_prestamos_ui()
    id_gestion = validar_entero('ID del préstamo a gestionar: ')
    registros = repo.obtener_todos()
    
    for p in registros:
        if p.get('id') == id_gestion:
            op = validar_menu("1. Aprobar/Gestionar\n2. Rechazar\nSeleccione: ", 1, 2)
            if op == 1:
                gestionar(p.get('herramienta', {}).get('id'), p)
            else:
                rechazar(p)
            
            repo.actualizar_registros(registros)
            print("Estado actualizado correctamente.")
            return
    print("ID de préstamo no encontrado.")