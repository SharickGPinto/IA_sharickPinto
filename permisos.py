from validaciones import validar_menu

def login():
    while True:
        op= validar_menu('''
                    ******************************************
                    * *
                    * SISTEMA DE INICIO DE SESIÓN *
                    * "Tu Amigo del Vecindario" *
                    * *
                    ******************************************
                            [  ◢◤  SEGURIDAD  ◥◣  ]

                    Por favor, identifícate para continuar:

                        1. Ingresar como ADMINISTRADOR
                        2. Ingresar como RESIDENTE
                        3. SALIR DEL SISTEMA

                    ------------------------------------------
                    >>> Selecciona tu perfil (1-3): ''',1,3)
        match op:
            case 1:
                print("-" * 15)
                print("[ZONA DE ACCESO RESTRINGIDO: ADMIN]")
                print("-" * 15)
                contrasenia= input('Introduce la clave de seguridad para continuar: ')
                if contrasenia == 'admin123':
                    return 'admin'
                else:
                    print('Contreseña incorrecta, sera regresado al menu de ingreso')
            case 2:
                print("-" * 15)
                print("[ ÁREA DE RESIDENTES: MI HOGAR ]")
                print("-" * 15)
                contrasenia= input('Introduce la clave de seguridad de residente: ')
                if contrasenia == 'residente123':
                    return 'residente'
                else:
                    print('Contreseña incorrecta, sera regresado al menu de ingreso')

            case 3:
                print('''
                    __________________________________________
                    /                                          \\
                    |    👋 ¡HASTA LUEGO, VECINO!              |
                    |__________________________________________/
                    
                    La sesión se ha cerrado correctamente.
                    Gracias por cuidar de nuestra comunidad.
                    
                    [ ESTADO: SISTEMA FUERA DE LÍNEA ]
                    __________________________________________
                    ''')
                break