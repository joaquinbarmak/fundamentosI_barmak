# ej1

'''
lista_super = ["tomate", "fideos", "arvejas", "detergente", "jabon", "alcohol"]
try:
    lista_super + "arroz"
except:
    print("no puedo agregar arroz")
'''

# Es correcto el uso del try...except? Que cosa/s le modificarias?

#  No, no es correcto porque falta el tipo de error. El print del except deberia ser explicativo de por que es un error.
#  Ademas que seria lista_super.append('arroz')

# ej2

def ejercicio2 (lista_n, n):
    lista_nueva = []
    try:
        for numero in lista_n:
            lista_nueva.append(numero/n)
        return (lista_nueva)
    except TypeError:
        return('Hay un string en la lista, aca solo admitimos numeros')
    except ZeroDivisionError:
        return('No se puede dividir por 0')

print(ejercicio2([2,4,6,8], 2))
print(ejercicio2([2,4,'6',8], 2))
print(ejercicio2([2,4,6,8], 0))
print(ejercicio2([2,4,'6',8], 0))

# ej 3
''' Resolucion Franco Puricelli
def es_positivo (lista_n):
    lista_nueva = []
    for numero in lista_nueva:
        if numero < 0 :
            raise Exception(f'{numero} no es positivo')
                        #  (str(i) + ' no es positivo')
        if numero > 0:
            lista_nueva.append(numero)
'''

def ejercicio3 (lista_n, n):
    if n > 0:
        lista_n.append(n)
        print(lista_n)
    elif n == 0:
        raise Exception('n no puede ser 0')
    elif n == str(n):
        raise Exception('n no puede ser un string')
    else:
        raise Exception('n no puede ser negativo')
'''
ejercicio3([2, 4, 6, 8], 10)
ejercicio3([2, 4, 6, 8], '0')
ejercicio3([2, 4, 6, 8], 0)
ejercicio3([2, 4, 6, 8], 0)
'''