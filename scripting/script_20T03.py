#!/bin/python3
import os
import sys
# == import os, sys

usuario = sys.argv[1] #sys.arg toma los argumentos que le pasamos al string por consola
                        # [1] significa que siempre voy a tomar el primero
                        # es decir leo solo la primer palabra que escriben en la terminal
def saludador(n):
    return "Hola " + n

if __name__ == "__main__":
    print(saludador(usuario))

#tarea swap.py 