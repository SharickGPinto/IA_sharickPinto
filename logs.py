from datetime import datetime
from gestionar_txt import guardar_txt

# Configuración de logs
ARCHIVO_LOGS = 'historial.txt'

def registrar_evento(mensaje: str):
    """
    Registra una acción en el sistema con un formato estandarizado:
    [ISO-DATETIME] ACCIÓN
    """
    # Usamos un formato de fecha ISO 8601 que es el estándar en industria
    fecha_formateada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Construimos un log profesional
    log_entry = f"[{fecha_formateada}] {mensaje.upper()}"
    
    # Mostramos en consola para el administrador
    print(f"LOG: {log_entry}")
    
    # Persistencia
    guardar_txt(ARCHIVO_LOGS, log_entry)

def historial_acciones_ui():
    """
    Función de utilidad para mostrar el historial completo en consola
    si el administrador lo solicita.
    """
    from gestionar_txt import cargar_txt
    contenido = cargar_txt(ARCHIVO_LOGS)
    
    if not contenido:
        print("El historial está vacío.")
    else:
        print("\n--- HISTORIAL DE OPERACIONES ---")
        print(contenido)