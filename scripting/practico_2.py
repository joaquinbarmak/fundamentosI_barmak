#ej 1
def controlador (lista):
    for palabra in lista:
        if palabra == 'control' or palabra == 'Control':
            lista.append('revisado')
            lista.remove(palabra)
    return lista

#print(controlador(['hola', 'mundo', 'control', 'adios']))

#ej 2
def eliminador (lista):
    lista.pop(0)
    return lista

#print(eliminador(['hola', 'mundo', 'control', 'adios']))

#ej 3
def ojo_de_halcon (lista, elemento):
    for cosa in lista:
        if cosa == elemento:
            lista.remove(cosa)
    return lista

#print(ojo_de_halcon(['hola', 'mundo', 'control', 'adios'], 'adios'))

#ej 4
def switch_de_listas (lista1, lista2, elemento):
    for sumsum in lista1:
        if sumsum == elemento:
            lista1.remove(sumsum)
            lista2.append(sumsum)
    for sumsum2 in lista2:
        if sumsum2 == elemento:
            lista1.append(sumsum2)
            lista2.remove(sumsum2)
    return lista1, lista2

#print(switch_de_listas(['hola', 'mundo', 'control', 'adios'],['aquello', 'claro', 'arancel', 'pato'], 'pato'))

#ej5
def par(num):
    return num % 2 == 0 and num != 0

def parisiano (lista):
    for numero in lista:
        return par(numero) == True

print(parisiano([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))