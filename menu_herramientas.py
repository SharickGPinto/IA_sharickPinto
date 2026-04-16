from validaciones import validar_menu
from gestionar_herramienta import (
    guardar_herramienta_ui,
    actualizar_herramienta_ui,
    listar_herramientas_ui,
    buscar_herramienta_ui,
    eliminar_herramienta_ui
)
from logs import registrar_evento

def menu_herramienta():
    """
    Controlador de interfaz para la administración del inventario de herramientas.
    Conecta la interacción del usuario con la lógica de negocio y auditoría.
    """
    
    MENU_TEXTO = """
    ==========================================================
              🛠️  INVENTARIO: GESTIÓN DE HERRAMIENTAS
    ==========================================================
    
    Panel de Control - Selecciona una acción:
    
        [1] Registrar nueva herramienta
        [2] Actualizar datos existentes
        [3] Listar inventario completo
        [4] Buscar herramienta específica
        [5] Eliminar del sistema
        [6] Volver al menú anterior
    
    ==========================================================
    >>> Digita tu opción (1-6): """

    while True:
        opcion = validar_menu(MENU_TEXTO, 1, 6)
        
        # Separador visual para limpiar la salida de los datos
        print("\n" + "-"*45)

        match opcion:
            case 1:
                guardar_herramienta_ui()
                registrar_evento('INVENTARIO: Registro de nueva herramienta')
            case 2:
                actualizar_herramienta_ui()
                registrar_evento('INVENTARIO: Actualización de datos técnica')
            case 3:
                listar_herramientas_ui()
            case 4:
                buscar_herramienta_ui()
            case 5:
                eliminar_herramienta_ui()
                registrar_evento('INVENTARIO: Baja de herramienta del sistema')
            case 6:
                print("Regresando al panel principal...")
                break
        
        # Pausa de cortesía para lectura de datos (excepto al salir)
        if opcion != 6:
            input("\nPresione ENTER para continuar...")