from validaciones import validar_menu
from gestionar_usuario import (
    guardar_usuario_ui,
    actualizar_usuario_ui,
    listar_usuarios_ui,
    buscar_usuario_ui,
    eliminar_usuario_ui
)
from logs import registrar_evento

def menu_usuario():
    """
    Controlador de interfaz para la administración de usuarios y residentes.
    Centraliza las operaciones de registro, consulta y mantenimiento del directorio.
    """
    
    MENU_TEXTO = """
    ==========================================================
                DIRECTORIO: GESTIÓN DE USUARIOS
    ==========================================================
    
    Administración de Miembros del Vecindario:
    
        [1]  Registrar nuevo usuario
        [2]  Actualizar datos existentes
        [3]  Listar todos los residentes
        [4]  Buscar usuario específico
        [5]  Eliminar del sistema
        [6]  Volver al menú anterior
    
    ==========================================================
    >>> Selecciona una gestión (1-6): """

    while True:
        opcion = validar_menu(MENU_TEXTO, 1, 6)
        
        print("\n" + "-"*45) # Separador visual

        match opcion:
            case 1:
                guardar_usuario_ui()
                registrar_evento('USUARIO: Registro de nuevo miembro en el sistema')
            case 2:
                actualizar_usuario_ui()
                registrar_evento('USUARIO: Actualización de información de contacto/residencia')
            case 3:
                listar_usuarios_ui()
            case 4:
                buscar_usuario_ui()
            case 5:
                eliminar_usuario_ui()
                registrar_evento('USUARIO: Baja de usuario del directorio')
            case 6:
                print("Regresando al menú principal...")
                break
        
        if opcion != 6:
            input("\nPresione ENTER para continuar...")