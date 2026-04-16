from validaciones import validar_menu
# Importamos las funciones UI que refactorizamos en el módulo de consultas
from gestionar_consultas import (
    stock_minimo_ui,
    activos_completados_ui,
    historial_usuarios_ui,
    frecuencia_uso_ui
)

def menu_reportes():
    """
    Controlador principal de la sección de analítica y reportes.
    Mantiene la interfaz limpia y redirige a los servicios correspondientes.
    """
    
    # Definimos el diseño del menú como una constante para facilitar su edición
    MENU_TEXTO = """
    ==========================================================
                REPORTE Y CONSULTAS GENERALES
    ==========================================================
    
    Filtros de información disponibles:
    
        [1]  Stock mínimo (Baja disponibilidad)
        [2]  Solicitudes en proceso / completadas
        [3]  Buscar historial por usuario
        [4]  Ranking: Herramientas más usadas
        [5]  Ranking: Usuarios con más préstamos
        [6]  Volver al menú anterior
    
    ==========================================================
    >>> Seleccione una opción: """

    while True:
        opcion = validar_menu(MENU_TEXTO, 1, 6)
        
        print("\n" + "-"*30) # Separador visual para la salida del reporte
        
        match opcion:
            case 1:
                stock_minimo_ui()
            case 2:
                activos_completados_ui()
            case 3:
                historial_usuarios_ui()
            case 4:
                # Reutilizamos la función genérica pasando el tipo
                frecuencia_uso_ui('herramienta')
            case 5:
                # Reutilizamos la función genérica pasando el tipo
                frecuencia_uso_ui('usuario')
            case 6:
                print("Regresando al menú principal...")
                break
        
        input("\nPresione ENTER para continuar...") # Pausa para que el usuario lea el reporte