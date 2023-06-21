import requests
respuesta = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
datos = respuesta.json()
respuesta1 = requests.get('https://pokeapi.co/api/v2/pokemon')
datos1 = respuesta1.json()
# ej 1
# el dominio que estamos consultando en pokeapi.co

# ej 2

print(respuesta.status_code)
# devuelve el status_code 200 (todo OK)

print(respuesta.headers['Content-Type']) # .keys() --> sirve como diccionario.
# utf-8                                    .headers --> sirve como diccionario que no discrimina entra mayus y minus.

print(datos['forms'])
# tiene 1 forma

# ej 3 

print(datos1['count'])
# hay 1281 pokemones

# ej 6
respuesta2 = requests.get('https://pokeapi.co/api/v2/pokemon/sylveon')
with open('ficha_tecnica_pokemons.txt', 'wb') as ficha:
    ficha.write(respuesta.content)
    ficha.write(b'\n')
    ficha.write(respuesta2.content)

# punto 2
# ej 1
response = requests.get('https://jsonplaceholder.typicode.com/todos')
data = response.json()

# ej 3
