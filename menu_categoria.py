from validaciones import validar_menu
from gestionar_categoria import (
    guardar_categoria_ui,
    actualizar_categoria_ui,
    listar_categorias_ui,
    buscar_categoria_ui,
    eliminar_categoria_ui
)
from logs import registrar_evento

def menu_categoria():
    """
    Controlador de interfaz para la gestión de categorías.
    """
    
    MENU_TEXTO = """
    ==========================================================
                CONFIGURACIÓN: CATEGORÍAS
    ==========================================================
    
    Organización de Herramientas del Barrio:
    
        [1] Registrar nueva categoría
        [2] Actualizar datos existentes
        [3] Listar todas las categorías
        [4] Buscar categoría específica
        [5] Eliminar categoría
        [6] Volver al menú anterior
    
    ==========================================================
    >>> Selecciona una opción (1-6): """

    while True:
        opcion = validar_menu(MENU_TEXTO, 1, 6)
        
        print("\n" + "-"*40)

        match opcion:
            case 1:
                guardar_categoria_ui()
                registrar_evento('CATEGORÍA: Se ha creado una nueva categoría')
            case 2:
                actualizar_categoria_ui()
                registrar_evento('CATEGORÍA: Se ha actualizado una categoría')
            case 3:
                listar_categorias_ui()
            case 4:
                buscar_categoria_ui()
            case 5:
                eliminar_categoria_ui()
                registrar_evento('CATEGORÍA: Se ha eliminado una categoría')
            case 6:
                print("Regresando al menú anterior...")
                break
        
        if opcion != 6:
            input("\nPresione ENTER para continuar...")