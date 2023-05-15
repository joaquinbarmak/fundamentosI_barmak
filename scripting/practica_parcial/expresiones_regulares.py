#Escribir en funciones que, dado un String, permitan:

#a) Obtener la lista de subsecuencias delimitadas por "X" e "Y" que incluyan la subsecuencia "ab".
#   Por ejemplo para XbaaaYjXababYqXbabbbbaaYqXffeeY, hay que devolver ["abab", "babbbaa"].

import re

def xaby (string):
    return re.findall('X([^XY]*ab[^XY]*)Y', string)

print(xaby('XbaaaYjXababYqXbabbbbaaYqXffeeY'))

"""
b) Onomatopopih esta aprendiendo expresiones regulares y le pidieron construir una funcion que sea capaz de 
extraer la lista de substrings delimitadas por los patrones 'ag' y 'cta' y no incluyan numeros. 
Revisa su codigo propuesto y marca con una x las opciones correctas. JUSTIFICA tus respuestas.

def funcionDeExpresiones_Regulares():
    return re.findal("ag(\d. *?)cta")
    
-El nombre de la funcion de Onomatopopih respeta las convenciones de nombres de Python: 

NO, ya que lo ideal es que este todo en minusculas 

-La funcion lanza NameError al ser ejecutada

-La funcion lanza SyntaxError al ser ejecutada:

NO exactamante, a mi me tira un TypeError, porque primero, no le damos un string como argumento
cuando inicializamos la funcion, ademas que como no ponemos un string de argumento, no se pone
el segundo item de la funcion re.findall, la cual por cierto esta mal escrita.

-Una vez corregida la funcion, cuando se la invoca usando el texto "'aabocaggaaactazu4iggaasag24gra 1ndecta' devuelve
['gaaa"')
-Una vez corregida la funcion, cuando se la invoca usando el texto "aabocaggaaactazu4iggaasag24gra 1ndecta' devuelve
[24gra1nde')
 """

def funcionDeExpresiones_Regulares():
    return re.findal("ag(\d. *?)cta")

#print(funcionDeExpresiones_Regulares('aabocaggaaactazu4iggaasag24gra 1ndecta'))

def funcion_de_expresiones_regulares(string):
    return re.findall("ag([^\d]*)cta", string) #    "ag([^\d]*)cta"

print(funcion_de_expresiones_regulares('aabocaggaaactazu4iggaasag24gra 1ndecta'))


#ejercicio 5

def numero_especifico(numero, string):
    return bool(re.search('^' +str(numero), string))

print(numero_especifico(10, '11 ben'))

#ejercicio 7

def solo_mayuminus(string):
    return bool(re.search('^[\w\s]+$', string))

print(solo_mayuminus('hola 2354 que  $s'))

#ej 9
def entre_guiones (string):
    return re.findall('-(.*?)-', string)

print(entre_guiones("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"))