# Planteamiento del problema:

En muchos barrios existe la costumbre de compartir herramientas entre vecinos para evitar que cada persona tenga que comprarlas todas. El problema es que, con el tiempo, se pierde el control: algunas herramientas no se devuelven a tiempo, otras se dañan y no se sabe quién las tiene, o simplemente no hay registro claro de cuántas hay disponibles.

La junta comunal de tu barrio ha decidido organizar este proceso mediante un programa de consola que registre las herramientas, los vecinos y los préstamos realizados. Con esta solución, esperan que cualquier integrante de la comunidad pueda consultar la información sin depender de cuadernos ni llamadas telefónicas.

## Requerimientos
### Gestión de herramientas
    Cada herramienta debe registrar: id, nombre, categoría (ej. construcción, jardinería), cantidad disponible, estado (activa, en reparación, fuera de servicio) y valor estimado.
    El programa debe permitir: crear, listar, buscar, actualizar y eliminar o inactivar herramientas.
### Gestión de usuarios
    Cada vecino debe registrar: id, nombres, apellidos, teléfono, dirección y tipo de usuario (ej. residente, administrador).
    Operaciones: crear, listar, buscar, actualizar y eliminar usuarios.
### Gestión de préstamos
    Al registrar un préstamo se debe guardar: id del préstamo, usuario, herramienta, cantidad, fecha de inicio, fecha estimada de devolución, estado y observaciones.
    El sistema debe verificar disponibilidad de la herramienta y ajustar la cantidad en stock.
    Cuando se devuelva la herramienta, se debe actualizar el estado del préstamo y restaurar la cantidad disponible.
### Consultas y reportes
    Herramientas con stock bajo (por ejemplo, menos de 3 unidades).
    Préstamos activos y vencidos.
    Historial de préstamos de un usuario.
    Herramientas más solicitadas por la comunidad.
    Usuarios que más herramientas han solicitado.
### Registro de eventos (logs)
    Todo error o evento relevante (ejemplo: intentar prestar más herramientas de las disponibles) debe quedar registrado en un archivo de texto para seguimiento de la administración.
### Permisos a manejar:
    Administrador: Se encargará de registrar a los usuarios y sus herramientas con el fin de evitar suplantación de identidad.
    Usuario: Puede consultar el estado de las herramientas, cuando quedará disponible y quien la posee. Del mismo modo, puede crear una solicitud de herramienta que debe ser aprobada por el administrador. 
