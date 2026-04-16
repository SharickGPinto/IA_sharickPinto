from validaciones import validar_menu
from gestionar_prestamo import (
    guardar_prestamo_ui,
    consultar_prestamos_ui
)

def menu_prestamo_residente():
    """
    Controlador de interfaz para los usuarios residentes.
    Proporciona un acceso simplificado para solicitar herramientas y revisar historial personal.
    """
    
    MENU_TEXTO = """
    ==========================================================
                  ÁREA RESIDENTE: MIS PRÉSTAMOS
    ==========================================================
    
    ¿En qué podemos ayudarte hoy?
    
        [1]  Solicitar un nuevo préstamo
        [2]  Consultar el estado de mis préstamos (Historial)
        [3]  Volver al menú anterior
    
    ==========================================================
    >>> Seleccione una opción: """

    while True:
        opcion = validar_menu(MENU_TEXTO, 1, 3)
        
        print("\n" + "-"*45)

        match opcion:
            case 1:
                # Inicia el flujo de selección de herramienta y fechas
                guardar_prestamo_ui()
            case 2:
                # Llamamos a la función de consulta pasando el filtro de usuario
                # Esto asegura que el residente solo vea SUS datos
                consultar_prestamos_ui(por_usuario=True)
            case 3:
                print("Cerrando sesión de residente...")
                break
        
        if opcion != 3:
            input("\nPresione ENTER para continuar...")