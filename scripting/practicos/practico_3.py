import re

#ej 1
def caracter_permitido(string):
    return bool(re.search('[a-zA-z]', string))

print(caracter_permitido('ABCja578'))

#ej15

#def mail_valido(string):
    #return bool(re.search('^\w+[.-_]?\w*@[a-z]+[.]?[a-z]?$', string))

#print(mail_valido('joaquinbarmak@gmail.com'))

#ej 15 correcto

#def mail_correcto(string):
    #return bool(re.search('^\w+[.-]?\w*@[a-z]+[.][a-z]+[.]?[a-z]?',string))
#print(mail_correcto('salva-burgos@gmail.com'))

# EXPLICACIÓN PATRÓN:
# ^\w+[.-]?\w* --> inicia con 1 o mas caracteres alfanumericos, que pueden estar seguidos o no de u '.' o '-', a lo que le pueden seguir o no otros caracteres alfanumércios .
# @ <-- le debe seguir una @ obligatoriamente
# [a-z]+[.][a-z]+ <-- a continuacion el dominio (incluye solo letras minusculas ej: 'gmail'). Luego separa un '.' obligatoriamente del 'com' o 'edu'
# [.]?[a-z]? <-- puede incluir el '.ar' por ejemplo. NO es necesacrio que lo incluya
#def mail_correcto(string):
   # return bool(re.search('^\w+[.-]?\w*@[a-z]+[.][a-z]+[.]?[a-z]?',string))
#print(mail_correcto('salva-burgos@gmail.com'))

# EXPLICACIÓN PATRÓN:
# ^\w+[.-]?\w* --> inicia con 1 o mas caracteres alfanumericos, que pueden estar seguidos o no de u '.' o '-', a lo que le pueden seguir o no otros caracteres alfanumércios .
# @ <-- le debe seguir una @ obligatoriamente
# [a-z]+[.][a-z]+ <-- a continuacion el dominio (incluye solo letras minusculas ej: 'gmail'). Luego separa un '.' obligatoriamente del 'com' o 'edu'
# [.]?[a-z]? <-- puede incluir el '.ar' por ejemplo. NO es necesacrio que lo incluya