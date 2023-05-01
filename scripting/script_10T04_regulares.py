import re

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
#patron = "a[a-z]{3}"

#print(re.search(patron, texto))
#print(re.match(patron, texto))
#print(re.findall(patron, texto))
#print(re.search(patron, texto).group())

#print(re.sub(patron, "###", texto))

#ej1
def caracteres_permitidos(string):
    return bool(re.search('[a-zA-Z0-9.]', string))

#print(caracteres_permitidos('%'))

#bool(4) ==> True

#ej2
def caracteres_permitidos_not(string):
    return not bool(re.search('[a-zA-Z0-9.]', string)) #NO ANDA

#print(caracteres_permitidos_not('hola'))

#ej3
def encontrar_patron(string):
    patron = 'he*'
    if re.search(patron, string) is not None:
        return 'Se encontro el patron'
    else:
        return 'No se encontro el patron'

#print(encontrar_patron('h'))

#ej3
def encontrar_patron2(string):
    patron = 'he+'
    if re.search(patron, string) is not None:
        return 'Se encontro el patron'
    else:
        return 'No se encontro el patron'

#print(encontrar_patron2('he'))

#ej3
def encontrar_patron3(string):
    patron = 'he?'
    if re.search(patron, string) is not None:
        return 'Se encontro el patron'
    else:
        return 'No se encontro el patron'

#print(encontrar_patron3('eh'))

#ej3
def encontrar_patron4(string):
    patron = 'he{2,3}'
    if re.search(patron, string) is not None:
        return 'Se encontro el patron'
    else:
        return 'No se encontro el patron'

#print(encontrar_patron4('heeeeeyo'))

#ej4
def palabras_unidas(string):
    patron = '^[a-z]+_[a-z]+$'
    if re.search(patron, string) is not None:
        return 'Patron encontrado'
    else:
        return 'Patron no encontrado'

#print(palabras_unidas('hola que onda perri'))

#ej8
def extraer_numeros(string):
    resultado = re.split('\D+', string)
    for elemento in resultado:
        print(elemento)

#extraer_numeros('Hoy movimos 10 cajas de lugar, en 3 edificios distintos para llevar a 12 casas')

#ej9
def extraer_entre_guiones(string):
    return re.findall(r'-(.*?)-', string)

#print(extraer_entre_guiones('hoy estuvimos trabajando con re -regular expressions- via -VSCode-')) 

#ej11
def dos_P(lista):
    for elemento in lista:
        resultado = re.match('(P\w*)\W(P\w*)', elemento)
        if resultado is not None:
            print(resultado.group())

lista_ej = ['Practica Python', 'Practica C++', 'Practica Portnite']

dos_P(lista_ej)