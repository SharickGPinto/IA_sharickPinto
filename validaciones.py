def validar_entero(mensaje):
    while(True):
        try:
            dato=int(input(mensaje))
            while(dato<=0):
                dato=int(input('Error. Ingrese un numero positivo: ')) # 
            return dato
        except Exception:
            print('Error, solo se admiten número entero.')

def validar_decimales(mensaje):
    while(True):
        try:
            dato=float(input(mensaje)) 
            while(dato<=0):
                dato=float(input('Error. Ingrese un numero positivo real: ')) # 
            return dato
        except Exception:
            print('Error, solo se admiten números decimales.')

def validar_texto(mensaje, cantidad_minima, cantidad_maxima):
    try:
        dato=input(mensaje)
        caracteres=len(dato.strip())
        while(caracteres<cantidad_minima or caracteres>cantidad_maxima or dato==None):
            dato=input('Error, no puede dejar el espacio en blanco: ')
        return dato
    except Exception:
        print('Error, solo se admite texto')

def validar_menu(mensaje,minimo,maximo):
    op=validar_entero(mensaje)
    while op<minimo or op>maximo:
        op=validar_entero('Error intentelo nuevamente: ')
    return op