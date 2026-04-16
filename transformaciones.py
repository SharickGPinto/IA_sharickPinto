from validaciones import validar_entero, validar_texto
from datetime import datetime,date,timedelta
from gestionar_json import *
from logs import historial



def transformar_estado(estado):
    if estado==1:
        return 'Activo'
    elif estado==2:
        return 'En reparación'
    else:
        return 'Inactiva'

def transformar_tipo(tipo):
    if tipo==1:
        return 'Residente'
    else:
        return 'Administrador'
    
def solicitar_fecha_inicio():
    anio=validar_entero('Ingrese el año de la solicitud: ')
    mes=validar_entero('Ingrese el mes de la solicitud: ')
    dia=validar_entero('Ingrese el dia de la solicitud: ')
    fecha_guardada= date(anio,mes,dia)
    return fecha_guardada


def gestionar(id,elemento):
    registros=cargar('herramientas.json')
    for elemento_herramienta in registros:
        if elemento_herramienta.get('id','Clave no encontrada')== id:
            if elemento_herramienta.get('cantidad')>=elemento.get('cantidad','Clave no encontrada'):
                cantidad_prestamo= elemento.get('cantidad','Clave no encontrada')
                cantidad_herramienta= elemento_herramienta.get('cantidad','Clave no encontrada')
                elemento_herramienta['cantidad']=  cantidad_herramienta - cantidad_prestamo
                elemento['estado']= 'Aceptada'
                elemento['observaciones'] = 'Se aprueba la solicitud, NO olivdes devolver la herramienta en su fecha destinada'
                aux={elemento_herramienta.get('cantidad','clave no encontrada')}
                print(f'Se acepta la solicitud debido a que hay stock de la herramienta, y queda un total de {aux} unidades de esa herramienta en Stock')
                guardar('herramientas.json',registros)
            else: 
                elemento['estado']= 'Rechazada'
                elemento['observaciones']= 'Se rechaza por no haber stock disponible'
                print('No se puede gestionar esta solicitud debido a que no hay suficiente Stock')
                historial('Se solicito un prestamo de herramienta pero fue rechazado por no haber suficiente stock solicitado')


def rechazar(elemento):
    elemento['observaciones']= validar_texto('Ingrese el motivo por el cual rechaza la solicitud de prestamo: ',1,100)
    elemento['estado']='Rechazada'




    
