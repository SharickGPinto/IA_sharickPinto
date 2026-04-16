from typing import List, Dict, Any, Optional
from gestionar_json import cargar
from validaciones import validar_menu, validar_entero

# --- CONSTANTES DE ARCHIVOS ---
PATH_HERRAMIENTAS = 'herramientas.json'
PATH_PRESTAMOS = 'prestamos.json'
PATH_USUARIOS = 'usuarios.json'

# --- CAPA DE SERVICIOS (LÓGICA) ---

class ReportService:
    """Clase encargada de filtrar y procesar datos sin interacción con consola."""
    
    @staticmethod
    def filtrar_por_stock(max_stock: int) -> List[Dict]:
        herramientas = cargar(PATH_HERRAMIENTAS)
        return [h for h in herramientas if h.get('cantidad', 0) <= max_stock]

    @staticmethod
    def filtrar_prestamos_por_estado(estados: List[str]) -> List[Dict]:
        prestamos = cargar(PATH_PRESTAMOS)
        return [p for p in prestamos if p.get('estado') in estados]

    @staticmethod
    def obtener_historial_usuario(usuario_id: int) -> List[Dict]:
        prestamos = cargar(PATH_PRESTAMOS)
        return [p for p in prestamos if p.get('usuario', {}).get('id') == usuario_id]

    @staticmethod
    def calcular_frecuencias(clave_entidad: str) -> Dict[int, int]:
        """Calcula cuántas veces aparece un ID (usuario o herramienta) en los préstamos."""
        prestamos = cargar(PATH_PRESTAMOS)
        frecuencias = {}
        for p in prestamos:
            entidad_id = p.get(clave_entidad, {}).get('id')
            if entidad_id is not None:
                frecuencias[entidad_id] = frecuencias.get(entidad_id, 0) + 1
        return frecuencias


# --- CAPA DE INTERFAZ (UI) ---

def imprimir_formato_prestamo(p: Dict):
    """Estandariza la visualización de préstamos para evitar código duplicado."""
    print(f"""
    {'*' * 40}
    ID PRÉSTAMO:    {p.get('id')}
    USUARIO:        {p.get('usuario', {}).get('nombre')} (ID: {p.get('usuario', {}).get('id')})
    HERRAMIENTA:    {p.get('herramienta', {}).get('nombre')} (ID: {p.get('herramienta', {}).get('id')})
    FECHAS:         {p.get('fecha_inicio')} --> {p.get('fecha_final')}
    ESTADO:         {p.get('estado')}
    OBS:            {p.get('observaciones')}""")

def stock_minimo_ui():
    limite = validar_entero("Ingrese la cantidad de stock máximo para la alerta: ")
    resultados = ReportService.filtrar_por_stock(limite)
    
    if not resultados:
        print(f"No hay herramientas con stock menor o igual a {limite}.")
        return

    for h in resultados:
        print(f"ID: {h.get('id')} | {h.get('nombre'):<20} | Cantidad: {h.get('cantidad')}")

def activos_completados_ui():
    op = validar_menu("1. En proceso\n2. Finalizados (Aceptada/Rechazada)\nSeleccione: ", 1, 2)
    estados = ['En proceso'] if op == 1 else ['Aceptada', 'Rechazada']
    
    prestamos = ReportService.filtrar_prestamos_por_estado(estados)
    if not prestamos:
        print(f"No se encontraron registros para los estados: {', '.join(estados)}")
        return

    for p in prestamos:
        imprimir_formato_prestamo(p)

def frecuencia_uso_ui(tipo: str):
    """Unifica la lógica de 'más usado' para Herramientas y Usuarios."""
    # Mapeo de configuración según el tipo
    config = {
        'herramienta': (PATH_HERRAMIENTAS, 'herramienta'),
        'usuario': (PATH_USUARIOS, 'usuario')
    }
    path, clave = config[tipo]
    
    entidades = cargar(path)
    frecuencias = ReportService.calcular_frecuencias(clave)
    
    print(f"\n--- REPORTE DE USO: {tipo.upper()}S ---")
    for entidad in entidades:
        e_id = entidad.get('id')
        veces = frecuencias.get(e_id, 0)
        if veces > 0:
            nombre = entidad.get('nombre')
            apellido = entidad.get('apellido', '') # Solo para usuarios
            print(f"ID: {e_id:<4} | {nombre} {apellido:<15} | Total Usos: {veces}")