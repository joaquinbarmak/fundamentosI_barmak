#!/bin/python3
'''
OPCION 1

with open('mi_nombre.txt', 'r') as mi_arch:
    with open('nuevo_archivo.txt', 'a') as nuevo:
        nuevo.write(mi_arch.readline(5))
'''

#OPCION 2

texto_leido = open('mi_nombre.txt', 'r').read()

texto_para_escribir = texto_leido [0:6]

with open('nuevo_arch.txt', 'a') as mi_arch:
    mi_arch.write(texto_para_escribir)