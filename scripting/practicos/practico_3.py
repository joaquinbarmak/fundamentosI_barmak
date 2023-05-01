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

#print(numericos('hoy tengo 18 anios y maniana 19'))

#ej 9
def entre_guiones(script):
    return re.findall('-(.*?)-', script)

#print(entre_guiones("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"))
#Cuando usamos el signo de pregunta asi, favorecemos los matches internos, no ve solo lo global
#si no pongo el signo va a devolver: -regular expression- en python -con VSCode- porque no veria los guiones en el medio
#No devuelve el "en python" porque ya uso el guion del comienzo para cerrar el anterior.

#ej 10
def substringer (string):
    return re.findall('(.*?)[@|&](.*?)', string)

#print(substringer('ic@ie f&rjv@ninf'))

#ej 11
def dos_p(lista):
    for elemento in lista:
        resultado = re.match('(P\w*)\W(P\w*)', elemento)
        if resultado is not None:
            print(resultado.group())

#print(dos_p(["Practica Python", "Practica C++", "Practica Fortran"]))

#ej 12
def reemplazador(string):
    return re.sub('[\s_:]', '|', string)

#print(reemplazador("Nuestro _main_ es asi:"))

#ej 13
def guionizador(string):
    return re.sub('^[\W]{2}', '_', string)

#print(guionizador("@@@Nuestro @mail^ es asi:"))

#ej 14
def espaciador(script):
    return re.sub('[\s]', ';', script)

#print(espaciador('hola que onda               vo'))

#ej 15
def validador(script):
    return bool(re.search('^\w+[.-]?\w*@[a-z]+[.][a-z]+[.]?[a-z]?$', script))

print(validador('joaquinbarmak1@gmail.com'))