from validaciones import validar_menu
from gestionar_prestamo import (
    gestionar_prestamo_ui,
    buscar_prestamo_ui,
    listar_prestamo_ui,
    eliminar_prestamo_ui
)
from logs import registrar_evento

def menu_prestamo_admin():
    """
    Controlador de interfaz para la administración de préstamos.
    Permite a los administradores gestionar solicitudes, auditar y limpiar registros.
    """
    
    MENU_TEXTO = """
    ==========================================================
                LOGÍSTICA: GESTIÓN DE PRÉSTAMOS
    ==========================================================
    
    Panel de Control de Préstamos y Devoluciones:
    
        [1] Gestionar préstamos (Aprobar/Rechazar)
        [2] Buscar una solicitud específica
        [3] Ver todas las solicitudes
        [4] Eliminar registros de solicitudes
        [5] Volver al menú anterior
    
    ==========================================================
    >>> Seleccione una opción: """

    while True:
        opcion = validar_menu(MENU_TEXTO, 1, 5)
        
        print("\n" + "-"*45) # Separador de flujo

        match opcion:
            case 1:
                # Esta función interactúa con gestionar() y rechazar() internamente
                gestionar_prestamo_ui()
                registrar_evento('LOGÍSTICA: Gestión de estado en solicitud')
            case 2:
                buscar_prestamo_ui()
            case 3:
                listar_prestamo_ui()
            case 4:
                eliminar_prestamo_ui()
                registrar_evento('LOGÍSTICA: Eliminación de registro de préstamo')
            case 5:
                print("Regresando al panel administrativo...")
                break
        
        if opcion != 5:
            input("\nPresione ENTER para continuar...")