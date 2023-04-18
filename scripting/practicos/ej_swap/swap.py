# !/bin/python3

import os, sys

#una_de_dos = open('hola.txt', 'r').read()

os.rename('hola.txt', 'chau.txt') and os.rename('chau.txt', 'hola.txt')

# problema que tengo: se me borra uno de los archivos,
# aunque se realiza el cambio de nombres en el que no se borra