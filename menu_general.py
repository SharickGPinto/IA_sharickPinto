from validaciones import validar_menu
from menu_categoria import menu_categoria
from menu_herramientas import menu_herramienta
from menu_usuario import menu_usuario
from menu_prestamo_admin import menu_prestamo_admin
from menu_consultas import menu_reportes
from permisos import login
from gestionar_json import cargar
from logs import historial
from menu_prestamo_residente import menu_prestamo_residente

def menu_general():
    permiso=login()
    while True:
        if permiso == 'admin':
            op_menu_admin= validar_menu('''
                                        /\\______________/\\
                                        /  ¡BIENVENIDO A!  \\
                                        |      APP: TU       |
                                        |AMIGO DEL VECINDARIO|
                                        \\  ____________  /
                                        \\/            \\/

                                        ********* HOlA ADMIN **************
                                        Selecciona una opción:
                                        -----------------------
                                        1) Gestionar Herramientas
                                        2) Gestionar Categoria de Herramientas
                                        3) Gestionar Usuarios
                                        4) Gestionar Prestamos
                                        5) Consultar Reportes
                                        6) Salir
                                        -----------------------
                                        >>>''',1,6)
            match op_menu_admin:
                case 1:
                    if not cargar('categorias.json'):
                        print('NO SE PUEDE REALIZAR NINGUNA OPCIÓN HASTA INGRESAR UNA CATEGORIA')
                        historial('Se intento hacer un registro de Herramienta pero no hay categorias ')
                    else:
                        menu_herramienta()
                case 2:
                    menu_categoria()
                case 3:
                    menu_usuario()
                case 4:
                    if not cargar('usuarios.json') or not cargar('herramientas.json'):
                        print('NO SE PUEDE REALIZAR NINGUNA OPCIÓN DE PRESTAMO HASTA TENER REGISTRO DE USUARIOS Y HERRAMIENTAS')
                        historial('Se intento hacer una gestion de prestamo pero no hay usuarios o herramientas registradas ')
                    else:
                        menu_prestamo_admin()
                case 5:
                    if not cargar('prestamos.json') or not cargar('herramientas.json'):
                        print('NO SE PUEDE REALIZAR CONSULTAS DE REPORTE PORQUE NO HAY REGISTROS')
                        historial('Se intento hacer una consulta de reporte pero no hay registros en estos momentos ')
                    else:
                        menu_reportes()
                case 6:
                    print('''
                    __________________________________________
                    /                                          \\
                    |      ¡HASTA LUEGO, VECINO ADMIN!          |
                    |__________________________________________/
                    
                    La sesión se ha cerrado correctamente.
                    Gracias por cuidar de nuestra comunidad.
                    
                    [ ESTADO: SISTEMA FUERA DE LÍNEA ]
                    __________________________________________
                    ''')
                    break
        else:
            op_menu_residente=validar_menu(''' 
                                        /\\______________/\\
                                        /  ¡BIENVENIDO A!  \\
                                        |      APP: TU       |
                                        |AMIGO DEL VECINDARIO|
                                        \\  ____________  /
                                        \\/            \\/

                                        ******* HOlA VECINO ***************
                                        Selecciona una opción:
                                        -----------------------
                                        1) Gestionar Préstamos
                                        2) Salir
                                        -----------------------
                                        >>>''',1,2)
            match op_menu_residente:
                case 1:
                    if not cargar('usuarios.json') or not cargar('herramientas.json'):
                        print('No se puede solicitar un prestamo porque no hay registros de herramienta y usuarios')
                        print('Contacte al administrador para registrar usuarios y herramientas')
                        historial('Se intento realizar una solicitud de prestamo pero no se pudo porque no hay registros en usuarios y herramientas')
                    else:
                        menu_prestamo_residente()
                case 2:
                    print('''
                    __________________________________________
                    /                                          \\
                    |      ¡HASTA LUEGO, VECINO RESIDENTE!      |
                    |__________________________________________/
                    
                    La sesión se ha cerrado correctamente.
                    Gracias por cuidar de nuestra comunidad.
                    
                    [ ESTADO: SISTEMA FUERA DE LÍNEA ]
                    __________________________________________
                    ''')
                    break
                    
