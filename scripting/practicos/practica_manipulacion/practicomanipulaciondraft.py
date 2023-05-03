#ej 1
def odio_a_p(archivo):
    contador = 0
    with open(archivo, "r") as miarch1:
        for palabra in miarch1:
            if palabra[0] != 'P':
                contador+=1
    return contador

#print(odio_a_p('textoejemplo.txt'))

#ej 2
def imprimidor_de_lineas(numero, archivo):
    with open(archivo, 'r') as miarch2:
        for linea in range(numero):
            print(miarch2.readline())

imprimidor_de_lineas(2, 'textoejemplo.txt')

#ej 3
def leer_n_ultimas(numero, archivo):
    texto = open(archivo, 'r').readlines()

leer_n_ultimas(2, 'textoejemplo.txt')