#ej 1
def anterior(numero):
    return numero-1

def siguiente(numero):
    return numero+1

#print(anterior(5))

#ej 2
def doble (numero):
    return numero*2

#print(doble(5))

#ej 3
def doble_anterior(numero):
    return str(doble(anterior(numero))) + " " + str(doble(siguiente(numero)))

#print(doble_anterior(2))

#ej 4
def retirar_dinero(saldo, monto):
    return max(saldo-monto, 0)

#print(retirar_dinero(100,40))

#ej 5
def dia_de_la_semana_favorito(dia):
    return dia == "Sabado"

#print(dia_de_la_semana_favorito('Sabado'))

#ej 6
def rango_radio (longitud):
    return 223.0 <= longitud <= 586.8

#print(rango_radio(100))

#ej 7

def rango_radio_r (longitud):
    return 223.0 <= longitud <= 586.8 and longitud != 314.5

#print(rango_radio_r(314.6))

#ej 8
def tiene_descuento (edad):
    return edad <= 12 or edad >= 60

#print(tiene_descuento(70))

#ej 9
def xor (booleano1, booleano2):
    return booleano1 != booleano2

#print(xor(False, False))

#ej 10
def saludo (nombre, apellido):
    return "Hola " + nombre + ", en que andan los " + apellido + "?"

#print(saludo("Marcela", 'Roitman'))

#ej 11

def empieza_con_h (p):
    if p.startswith('h'):
        return len(p)

#print(empieza_con_h('zapatilla'))

#ej 12
def buenos(f):
    return f.startswith("Buenos") or f.startswith("Buenas")

#print(buenos('Buenos dias'))

#ej 13
def es_multiplo (num1, num2):
    return num2 % num1 == 0

#print(es_multiplo(3, 10))

#ej 14
def par_impar_cero (num):
    if num % 2 == 0 and num != 0:
        return "es par"
    elif num % 2 != 0:
        return "es impar"
    else:
        return "es cero"

#print(par_impar_cero(0))

#ej 15
def a_en_frase (frase):
    ases = 0
    for letra in frase:
        if letra == "a" or letra == "A":
            ases += 1
    return ases

#print(a_en_frase('hasta la vista bAby'))

#ej16
def cuantos_meses_me_quedan_de_vida (dinero):
    return dinero / 60000

print(cuantos_meses_me_quedan_de_vida(120000))