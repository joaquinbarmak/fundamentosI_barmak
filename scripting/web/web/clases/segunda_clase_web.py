import requests

respuesta = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
datos = respuesta.json()

'''

1) describir las partes de la url
2) que respuesta obtenes al hacer las get a esa url?
3) cual es el content type de esa respuesta?
4) cual es el status code de la respuesta?
5) cuantas habilidades (habilities) tiene este pokemon?

'''

# 1) pokeapi es la direccion, y despues se va esecificando en secciones cada vez mas especificas

# 2) Toda la api, con todos sus datos.

#print(datos) --> todos los datos en bruto
#print(datos.keys()) # --> los titulos de los datos que me va a dar


# 3) application/json; charset=utf-8 --> el tipo de dato es lo que esta despues de la barra (json)

#print(respuesta.headers['Content-Type'])

# 4) Status Code = 200

#print(respuesta.status_code)

# 5) Abilidades = 2

#print(len(datos['abilities']))




respuesta2 = requests.get('https://pokeapi.co/api/v2/ability/150/')
datos2 = respuesta2.json()