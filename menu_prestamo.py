from validaciones import validar_menu
from gestionar_prestamo import (
    guardar_prestamo_ui,
    gestionar_prestamo_ui,
    consultar_prestamos_ui,
    buscar_prestamo_ui,
    listar_prestamo_ui,
    eliminar_prestamo_ui
)
from logs import registrar_evento

def menu_prestamo():
    """
    Controlador central para el módulo de préstamos.
    Coordina todas las acciones de registro, consulta y administración.
    """
    
    MENU_TEXTO = """
    ==========================================================
                SISTEMA DE GESTIÓN DE PRÉSTAMOS
    ==========================================================
    
    Seleccione la acción a realizar:
    
        [1] Registrar nuevo préstamo (Solicitud)
        [2] Gestionar solicitudes (Aprobar/Rechazar)
        [3] Consultar mis préstamos (Vista Residente)
        [4] Buscar una solicitud específica (ID)
        [5] Listar todas las solicitudes (Vista Admin)
        [6] Eliminar registro de solicitud
        [7] Volver al menú principal
    
    ==========================================================
    >>> Opción: """

    while True:
        opcion = validar_menu(MENU_TEXTO, 1, 7)
        
        print("\n" + "-"*45)

        match opcion:
            case 1:
                guardar_prestamo_ui()
                registrar_evento("PRÉSTAMO: Creación de nueva solicitud")
            case 2:
                gestionar_prestamo_ui()
                registrar_evento("PRÉSTAMO: Gestión de estado administrativa")
            case 3:
                # Usamos el filtro de usuario para la vista de residente
                consultar_prestamos_ui(por_usuario=True)
            case 4:
                buscar_prestamo_ui()
            case 5:
                # Listado general administrativo
                listar_prestamo_ui()
            case 6:
                eliminar_prestamo_ui()
                registrar_evento("PRÉSTAMO: Eliminación de registro")
            case 7:
                print("Saliendo del módulo de préstamos...")
                break
        
        if opcion != 7:
            input("\nPresione ENTER para continuar...")