'''

Internet es la conexion cableada entre maquinas en el mundo.

La web es esa informacion que circula entre las maquinas.

Cliente y servidor son computadoras, y nosotros funcionamos como clientes (nuestra maquina).

El servidor aporta algo, mientras que el cliente es el que consume.
Siempre va a haber un pedido del cliente hacia el servidor.
Cliente pide, servidor responde.
El servidor no debe, o no deberia, hacer pedidos al cliente.

Contenido: datos, contenido, ...

Backend: servidor

Frontend: cliente 

Protocolo: un sistema de reglas que permiten que dos o mas entidades de un sistema de comunicacion 
           se comuniquen entre ellas para transmitir informacion.
'''
'''
Web app: - persiste (almacena, guarda) informacion.
         - tiene toda la logica que me permite a mi procesar y manejar la informacion.

Pagina Web: - no almacena informacion.
            - un archivo HTML expuesto en la nube.

Diferencia entre sitio y pagina web: un sitio son muchos archivos HTML interconectados.

Aplicacion Rest : cada recurso se va a corresponder con un url en particular.
Recurso: un tipo de item de la base de datos

'''
'''
Request --> un pedido a un servidor.

Verbos http --> disparan acciones particulares --> siempre hablando de aplicaciones Rest.

Post: verbo http asociado a persistir (guardar) datos de cero.

get: para obtener el contenido de una web o para realizar una peticion a un API.

delete: verbo asociado a borrar datos.

patch: verbo asociado a reescribir datos.

'''
'''

htts:// --> el protocolo que utilizamos para comunicarnos por la red
dominio --> el nombre con el cual voy a mapear una IP particular. Sirve como un alias del IP. (www.mercadolibre.com)
recurso --> las cosas que puedo consultar de la base de datos. (/aros-de-plata)

las URLs mapean recursos

diferencia entre path y url : una accede a datos mediante el internet (url), y a la otra de forma local (path).

'''


import requests # para ejecutar todo lo que es requests hay que usar python3 en la terminal

respuesta = requests.get('https://api.github.com/users/ajvelezrueda/orgs')
datos = respuesta.json()
# en cuantas organizaciones esta involucrado el usuario:
print(len(datos))
# en login sacamos la informacion del nombre del usuario:
print(len(datos[0]['login']))
#lista de nombres de las organizaciones en las que esta involucrada [TAREA]:
print(respuesta)
print(respuesta.headers)