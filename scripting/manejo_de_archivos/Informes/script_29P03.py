# !/usr/bin/env python3

import os, glob, sys

def ejercicio_rutas():
    os.chdir("Informes")
    txt = glob.glob("*.txt")
    cantidad_estado = []
    cantidad_lineas = []
    for archivo in txt:
        with open(archivo, 'r') as file:
            file_completa = file.read()
            cantidad_estado.append(file_completa.count('estado'))
            cantidad_lineas.append(file_completa.count('\n')) #asi cuento las lines(\n es enter)
        
    os.mkidr('Apellido')
    with open('Apellido/Lista.txt', 'w') as salida:
        for archivo in txt:
            with open(archivo, 'r') as file:
                #primer_linea = file.readline()
                #salida.write(primer_linea)
                salida.write(file.readline())
    return cantidad_estado, cantidad_lineas


ejercicio_rutas()