#!/usr/bin/python3

import re

#ej1
def caracteres_permitidos(string):
    return bool(re.search('[a-zA-Z]', string))

#print(caracteres_permitidos("]"))


'\w{4,}'
'[a-z]{3,6}'
'ab*'

'\d*'

'''
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.match(patron, texto))
'''
'''
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.search(patron, texto).group())
'''

#ej2
def minimo_todos(string):
    return bool(re.match('^[a-zA-Z0-9]+$', string))

#print(minimo_todos('aincin?ci'))

#ej 3
def hehehehe1 (string):
    return bool(re.search('he*', string))

#print(hehehehe1('el micael decia  '))

def hehehehe2 (string):
    return bool(re.search('he+', string))

#print(hehehehe2('el michael decia  h'))

def hehehehe3 (string):
    return bool(re.search('he?', string))
#print(hehehehe3('he e'))

def hehehehe4(string):
    return bool(re.search('he?', string))

#print(hehehehe4('he e'))

#ej 4
def buscaminas(string):
    return re.search('(\S)+_(\S)+', string).group()

#print(buscaminas('hola_que onda'))

#ej 5
def empieza_con(numero, string):
    return bool(re.search("^"+ str(numero),string))

#print(empieza_con(2, '4 b porque 3'))

#ej 6
def verificador(lista, string):
    for palabra in lista:
        if re.search(palabra , string):
            print("sip")
        else:
            print("nop")

#verificador(["hola","chau", "hello", "adios"], "hello  hola chau")

#ej 7
def discriminador(string):
    return bool(re.search('^[\w\s]+$', string))

#print(discriminador("este Es el ejem!plo 7"))

#ej 8
def numericos (string):
    return re.split('\D*', string)

print(numericos('hoy tengo 18 anios y maniana 19'))

#ej 9
